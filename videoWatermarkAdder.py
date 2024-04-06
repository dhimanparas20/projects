import cv2
import numpy as np
import os
import shutil
import subprocess
import random

# Function to overlay watermark on image with transparency
def overlay_watermarks(image, watermark, positions, alpha=0.8):
    for position in positions:
        x, y = position
        overlay = image[y:y+watermark.shape[0], x:x+watermark.shape[1]]
        image[y:y+watermark.shape[0], x:x+watermark.shape[1]] = cv2.addWeighted(overlay, alpha, watermark, 1 - alpha, 0)
    return image

# Load watermark image with transparency (4 channels)
watermark = cv2.imread('watermark.jpg', cv2.IMREAD_UNCHANGED)

# Load video
cap = cv2.VideoCapture('videodemo.mp4')

# Get video frame rate
fps = cap.get(cv2.CAP_PROP_FPS)

# Create directory for watermarked images
watermarked_dir = 'watermarked_images'
if os.path.exists(watermarked_dir):
    shutil.rmtree(watermarked_dir)
os.makedirs(watermarked_dir)

frame_count = 0
watermark_count = 10  # Number of watermarks per frame
alpha = 0.8  # Adjust transparency level (0.0 - fully transparent, 1.0 - fully opaque)
positions = []  # Initialize positions list
change_position_at = 0  # Frame number at which to change position

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Calculate the frame number at which to change position
    if frame_count == change_position_at:
        # Generate random positions for watermarks
        positions = [(np.random.randint(0, frame.shape[1] - watermark.shape[1]), np.random.randint(0, frame.shape[0] - watermark.shape[0])) for _ in range(watermark_count)]
        change_position_at += int(fps * 10)  # Change position every 5 seconds

    # Overlay watermarks with transparency
    frame_with_watermarks = overlay_watermarks(frame, watermark, positions, alpha)

    # Save the watermarked frame as an image
    cv2.imwrite(f'{watermarked_dir}/frame_{frame_count:04d}.png', frame_with_watermarks)
    frame_count += 1

cap.release()

# Extract audio using FFmpeg
subprocess.run(['ffmpeg', '-i', 'videodemo.mp4', '-vn', '-acodec', 'copy', 'audio.mp4'])

# Combine images into a video using FFmpeg with audio
subprocess.run(['ffmpeg', '-framerate', '60', '-i', f'{watermarked_dir}/frame_%04d.png', '-i', 'audio.mp4', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-strict', 'experimental', '-b:a', '192k', 'output_with_audio.mp4'])

# Remove temporary files
os.remove('audio.mp4')
shutil.rmtree(watermarked_dir)
