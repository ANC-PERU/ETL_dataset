# DOWNLOAD ENCERRONA MP3 AUDIO
from pytube import YouTube
from datetime import datetime
import os

today = datetime.today().strftime("%d/%m/%Y")
yt = YouTube(str(input("ENTER URL:\n")))
audio = yt.streams.filter(only_audio=True).first()
destination='mp3 audios/'
out_file = audio.download(output_path = destination)
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
print(today)
print("File downloaded......")