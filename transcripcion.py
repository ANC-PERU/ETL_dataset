import pandas as pd
import numpy as np
import whisper
import os


contenido = os.listdir('mp3 audios')
model = whisper.load_model("medium")
for audio in contenido:
    print("Transcribiendo:",audio)
    result = model.transcribe("mp3 audios/LO ADMITIÓ Dina quiere quedarse hasta el 2026 LaEncerrona.mp3",fp16=False)
    transcription = result['text']
    with open(f'transcriptiones/{audio}.txt','w') as f:
        f.write(transcription)

print('Done!!!')