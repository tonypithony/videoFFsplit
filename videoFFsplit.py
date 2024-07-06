import os, subprocess
from glob import glob


def split_video(input_file, output_prefix, duration):
    command = f"ffmpeg -i {input_file} -c copy -map 0 -segment_time {duration} -f segment {output_prefix}%03d.mp4"
    subprocess.call(command, shell=True)

filenames = glob("*.mp4")

for container in filenames:
	split_video(f"{container}", f"videodataset/{container[:-4]}_", 10)