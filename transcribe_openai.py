import openai
import os
from decouple import config 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')
openai.api_key = SECRET_KEY
audio_file = open("mp3 audios/LO ADMITIÓ Dina quiere quedarse hasta el 2026 LaEncerrona.mp3",'rb')
transcription = openai.Audio.transcribe("whisper-1",audio_file)
transcription_txt = transcription['text']
with open(f'transcriptions/openai_option.txt','w') as f:
        f.write(transcription_txt)