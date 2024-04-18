import datetime
import os
import requests
import subprocess
import time

# Input video file path
input_video_path = 'videodemo.mp4'

# Create output directory if it doesn't exist
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Define target resolutions
RESOLUTIONS = [(640, 480),(1280, 720), (1920, 1080)]
CWD = os.getcwd()

class Video:
    def __init__(self, s3_path,video_slug):
        self.s3_path = s3_path
        self.timestamp = datetime.datetime.now().isoformat()
        self.input_path = f"tmp_input_video_{self.timestamp}.mp4"
        self.output_paths = []
        self.video_slug = video_slug
        self.count = 0

    def import_video(self):
        # Send GET request to the video URL
        response = requests.get(self.s3_path, stream=True)

        # Check for successful response
        if response.status_code == 200:
            # Open the file in binary write mode
            with open(self.input_path, "wb") as f:
                # Stream the video content in chunks
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print("Video downloaded successfully to:", self.input_path)
        else:
            raise Exception(
                "Error downloading video. Status code:", response.status_code
            )

    def reduce(self):
        # Process each resolution
        for idx, (width, height) in enumerate(RESOLUTIONS, start=1):
            # Output video path
            output_video_path = f'{self.video_slug}_{width}x{height}.mp4'

            # FFmpeg command to resize video and retain audio
            ffmpeg_cmd = f'ffmpeg -i {self.input_path} -vf "scale={width}:{height}" -c:a copy {output_video_path}'

            # Execute FFmpeg command
            subprocess.run(ffmpeg_cmd, shell=True)

            print(f'Video resized to {width}x{height} and saved as {output_video_path}')
            self.output_paths.append(output_video_path)
            self.count +=1
            if self.count == 3:
              os.remove(self.input_path)
              self.count=0
        return self.output_paths   


    def release_processed_video(self):
        for file in self.output_paths:
            os.remove(file)

#USage
'''
obj = Video(s3_path="https://ungist.s3.ap-south-1.amazonaws.com/files/videodemo.mp4",video_slug="outputname")            
obj.import_video()
outputs  = obj.reduce()
print("------------------------------")
print([output for output in outputs])
print("------------------------------")
time.sleep(20)
obj.release_processed_video()
'''

