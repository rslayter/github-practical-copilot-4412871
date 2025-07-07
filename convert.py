
import os
# read mp3 files from the audio directory and list them
def read_mp3_files(directory):
    mp3_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.mp3'):
            mp3_files.append(filename)
    return mp3_files

print (read_mp3_files('audio'))