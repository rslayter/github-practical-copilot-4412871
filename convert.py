
import os
# create a function that reads audio files in the mp3 format
# from the audio directory and returns a list of them
def read_audio_files(directory):
    audio_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".mp3"):
            audio_files.append(os.path.join(directory, filename))
    return audio_files

print(read_audio_files("audio"))