import requests
from io import StringIO
import pandas as pd

# Extract goals
url_1 = "https://unstats.un.org/sdgapi/v1/sdg/Goal/List?includechildren=true"
response = requests.get(url_1)
data = response.json()
df = pd.DataFrame(data)
goals = list(df.code.unique())
del df
url_2 = 'https://unstats.un.org/sdgapi/v1/sdg/Goal/DataCSV'
for goal in goals:
    payload = {
        'goal': goal,              #GOAL
        'areaCodes': '604'      #PERU
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/octet-stream'
    }

    response = requests.post(url_2, data=payload, headers=headers)

    if response.status_code == 200:
        # Process the CSV data as needed
        csv_data = response.content.decode('utf-8')
        # Convert String into StringIO
        csvStringIO = StringIO(csv_data)
        del csv_data
        df = pd.read_csv(csvStringIO, sep=",")
        if df.shape[0]>0:
            df.to_csv(f'file/goal_{goal}_Peru.csv',index=None)
            del df
            print(f"Goal {goal} done...")

    else:
        print("Error: POST request failed with status code", response.status_code)
