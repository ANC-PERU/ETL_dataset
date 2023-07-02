import requests
from transformers import pipeline
from decouple import config 
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = config('API_KEY_NEWS_1')

# Set up News API credentials
api_key = SECRET_KEY
base_url = 'https://newsapi.org/v2/top-headlines'

# Set up Hugging Face summarization pipeline
summarizer = pipeline('summarization')

# SDGs topics and keywords
sdgs = [
    {'goal': 'No Poverty', 'keywords': ['poverty', 'inequality', 'income']},
    {'goal': 'Zero Hunger', 'keywords': ['hunger', 'malnutrition', 'food']},
    {'goal': 'Good Health and Well-being', 'keywords': ['health', 'well-being', 'disease']},
    {'goal': 'Quality Education', 'keywords': ['education', 'literacy', 'school']},
    {'goal': 'Gender Equality', 'keywords': ['gender', 'equality', 'empowerment']}
]

# Define the date range
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

# Fetch news articles for each SDG topic
for sdg in sdgs:
    print(f"Fetching news for {sdg['goal']} in Peru...\n")
    query = f'{sdg["keywords"][0]} AND Peru'
    parameters = {
        'apiKey': api_key,
        'q': query,
        'country': 'pe',
        'from': start_date.strftime('%Y-%m-%d'),
        'to': end_date.strftime('%Y-%m-%d'),
        'pageSize': 5
    }
    response = requests.get(base_url, params=parameters)
    print(response)
    articles = response.json()['articles']

    # Generate summaries for each article
    for article in articles:
        title = article['title']
        content = article['content']
        if content:
            print(f"Title: {title}")
            print("Summary:")
            summary = summarizer(content, max_length=300, min_length=30, do_sample=False)
            print(summary[0]['summary_text'])
            print("\n" + "-" * 50 + "\n")





