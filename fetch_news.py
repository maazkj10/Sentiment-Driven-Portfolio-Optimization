import requests
from datetime import datetime, timedelta

def fetch_broader_market_news(api_key, keywords, from_date, to_date, page_size=10):
    query = " OR ".join([f'"{keyword}"' for keyword in keywords])
    
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": from_date,
        "to": to_date,
        "pageSize": page_size,
        "apiKey": api_key,
        "language": "en",
        "sortBy": "relevancy",
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    articles = response.json().get("articles", [])
    headlines_by_day = {}
    
    for article in articles:
        published_date = article["publishedAt"].split("T")[0]
        if published_date not in headlines_by_day:
            headlines_by_day[published_date] = []
        headlines_by_day[published_date].append(article["title"])
    
    return headlines_by_day

def get_past_n_days(num_days):
    today = datetime.today()
    return [(today - timedelta(days=i)).strftime('%Y-%m-%d') for i in range(num_days)]
