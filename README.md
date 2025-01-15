Portfolio Optimization Using Sentiment Analysis

This project demonstrates a sentiment-driven portfolio optimization model, where sentiment analysis of news headlines is used to adjust the weights of different sectors in a portfolio. The goal is to dynamically optimize the portfolio by increasing exposure to sectors with positive sentiment and reducing exposure to sectors with negative sentiment.

## Project Overview

The system is designed to:
1. **Fetch news articles** for various sectors based on specific keywords.
2. **Classify the news** into relevant sectors such as Technology, Energy, Healthcare, etc.
3. **Perform sentiment analysis** on each sector's news to compute sentiment scores.
4. **Adjust portfolio weights** based on the sentiment scores, optimizing the sector allocation.

This approach allows for a more dynamic and responsive portfolio strategy, reacting to the latest market sentiment as reflected in the news.

## Key Components

### 1. **News Fetching**
   The system fetches news articles for each sector over the past 10 days. It uses a specified set of keywords related to each sector (e.g., “Technology”, “Energy”, “Healthcare”) to search for relevant news articles using an external news API.

### 2. **Sector Classification**
   Once the news is fetched, the system classifies each article into a sector (Technology, Finance, Energy, etc.) based on predefined keywords and machine learning models. This classification helps in analyzing how sentiment varies across different sectors.

### 3. **Sentiment Analysis**
   After classifying the news into respective sectors, the sentiment analysis model is used to compute sentiment scores for each sector. The sentiment score reflects the overall market sentiment for a particular sector based on the headlines. Positive scores indicate favorable sentiment, while negative scores reflect pessimistic views.

### 4. **Portfolio Adjustment**
   The portfolio consists of different sectors like Technology, Energy, Healthcare, Finance, etc. Based on the sentiment scores for each sector, the portfolio weights are adjusted. Positive sentiment will increase the exposure to that sector, while negative sentiment will reduce its weight in the portfolio. The adjusted portfolio provides a more data-driven approach to asset allocation.

## File Structure

- **`main.py`**: The main script that ties together the different components. It fetches news, classifies sectors, performs sentiment analysis, and adjusts portfolio weights.
- **`fetch_news.py`**: Contains the functionality to fetch news articles for various sectors over a specified time period.
- **`classify_sector.py`**: Provides the sector classification logic based on the content of the news articles.
- **`sentiment_analysis.py`**: Implements the sentiment analysis model to evaluate the sentiment of the classified news headlines.
- **`adjust_portfolio.py`**: Contains the logic to adjust the portfolio weights based on the sentiment analysis results.

## How It Works

### 1. Fetching News
The script fetches news for the last 10 days using the specified keywords for each sector (Technology, Finance, Energy, etc.). The news articles are retrieved from an external news API.

### 2. Classifying News
Once the news articles are fetched, the `classify_sector` function classifies the headlines into various sectors. Each headline is tagged with the appropriate sector (e.g., Technology, Energy, Healthcare).

### 3. Sentiment Analysis
Sentiment analysis is performed on the classified news headlines using a pre-trained sentiment analysis model. For each sector, sentiment scores are computed:
- **Positive Sentiment**: Indicates optimism about the sector.
- **Negative Sentiment**: Indicates pessimism about the sector.
- **Neutral Sentiment**: Indicates neutrality or lack of sentiment in the headlines.

### 4. Portfolio Adjustment
The adjusted portfolio is calculated based on the sentiment scores for each sector. A positive sentiment score leads to an increase in the portfolio's weight for that sector, while a negative sentiment reduces the weight.

### Example Workflow:

```python
from fetch_news import fetch_broader_market_news, get_past_n_days
import classify_sector
from sentiment_analysis import analyze_combined_sentiment
from adjust_portfolio import adjust_portfolio_weights

# Define the number of days for fetching news
past_days = get_past_n_days(10)

# Fetch the news headlines for the past 10 days
daily_headlines = fetch_broader_market_news(API_KEY, KEYWORDS, past_days)

# Classify the fetched headlines into sectors
sector_classification = classify_sector.classify_sector(daily_headlines)

# Perform sentiment analysis on the classified sectors
sentiment_results = analyze_combined_sentiment(sector_classification)

# Adjust the portfolio weights based on sentiment
adjusted_portfolio = adjust_portfolio_weights(sentiment_results, PORTFOLIO)

# Print adjusted portfolio weights
for sector, weight in adjusted_portfolio.items():
    print(f"{sector}: {weight:.2f}")


Sentiment Results:
{
    '2025-01-15': {'Technology': {'sentiment_score': 0.5, 'positive_prob': 0.7, 'negative_prob': 0.1, 'neutral_prob': 0.2}},
    '2025-01-14': {'Energy': {'sentiment_score': -0.3, 'positive_prob': 0.2, 'negative_prob': 0.6, 'neutral_prob': 0.2}},
    '2025-01-13': {'Finance': {'sentiment_score': -0.8, 'positive_prob': 0.1, 'negative_prob': 0.7, 'neutral_prob': 0.2}},
    ...
}


Adjusted Portfolio Weights:
    Technology: 0.25
    Energy: 0.15
    Healthcare: 0.20
    Finance: 0.10
    Geopolitical: 0.30

