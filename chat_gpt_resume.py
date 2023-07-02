from decouple import config 
import openai 
import os 
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('SECRET_KEY')

openai.api_key = SECRET_KEY
onlyfiles = os.listdir('transcriptions')
for filename in onlyfiles:
    file_txt = "transcriptions/" + filename
    text = open(file_txt,'r').read()
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=[
                                            {"role":"system", "content":"Eres un asistente de investigacion periodistica."},
                                            {"role":"user", "content":f"Genera un archivo json con cada tema con el resumen periodistico de este:{text[:3000]}"},
                                        ])
    a = response['choices'][0]["message"]["content"]
    print(a)
    json_resume = json.loads(a)
    print(json_resume)