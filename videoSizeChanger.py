import os
import subprocess

# Input video file path
input_video_path = 'videodemo.mp4'

# Create output directory if it doesn't exist
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Define target resolutions
resolutions = [(480, 360), (640, 480),(1280, 720), (1920, 1080)]

# Process each resolution
for idx, (width, height) in enumerate(resolutions, start=1):
    # Output video path
    output_video_path = f'{output_dir}/output_{width}x{height}.mp4'

    # FFmpeg command to resize video and retain audio
    ffmpeg_cmd = f'ffmpeg -i {input_video_path} -vf "scale={width}:{height}" -c:a copy {output_video_path}'

    # Execute FFmpeg command
    subprocess.run(ffmpeg_cmd, shell=True)

    print(f'Video resized to {width}x{height} and saved as {output_video_path}')

print('All videos resized successfully.')
