# Sentiment-Driven Portfolio Optimizer

## Overview
The **Sentiment-Driven Portfolio Optimizer** is an automated system that uses sentiment analysis on financial news headlines to adjust portfolio weights across different sectors. The model classifies news headlines into one of five sectors (such as Technology, Energy, Healthcare, Finance, and Geopolitical), performs sentiment analysis, and adjusts the weights of the portfolio based on the sentiment of each sector. This approach aims to help investors optimize their portfolio based on market sentiment.

The optimizer dynamically reallocates weights in the portfolio based on the sentiment (positive, neutral, or negative) observed for each sector, which could potentially improve returns and reduce risks.

## Project Structure

### `main.py`
This is the central script that integrates all the components of the optimizer. It:
- Fetches news articles from the past 10 days based on a list of predefined keywords.
- Classifies news headlines into one of five sectors: **Technology**, **Energy**, **Healthcare**, **Finance**, and **Geopolitical**.
- Analyzes the sentiment of the classified news for each sector and calculates sentiment scores.
- Adjusts the portfolio weights dynamically based on the sentiment scores for each sector.

#### Key Functions:
- **Fetching News**: It fetches headlines from a news API (e.g., NewsAPI) for a given period.
- **Classifying Sectors**: Headlines are classified based on predefined sector-specific keywords using the `classify_sector` function.
- **Sentiment Analysis**: The sentiment of the classified headlines is analyzed using a pre-trained model in the `analyze_combined_sentiment` function.
- **Adjusting Portfolio**: Portfolio weights are adjusted based on the sentiment analysis using `adjust_portfolio_weights`.

### `fetch_news.py`
This module contains functions to fetch news headlines for specific dates and keywords.

#### Key Functions:
- **`fetch_broader_market_news(API_KEY, keywords, from_date, to_date)`**: This function makes an API call to fetch market news articles between the specified date range (`from_date` to `to_date`). The articles are filtered using a list of keywords related to economic and financial factors.
  
- **`get_past_n_days(n)`**: This function calculates the dates for the last `n` days (in this case, 10 days) and returns them in the format required for the `fetch_broader_market_news` function.

### `classify_sector.py`
This file contains the logic for classifying news headlines into sectors. Each sector is associated with a list of keywords.

#### Key Function:
- **`classify_sector(headlines)`**: This function takes in a list of news headlines, checks for the presence of sector-related keywords, and classifies the headlines into appropriate sectors (Technology, Energy, Healthcare, Finance, and Geopolitical). It returns a dictionary mapping each sector to its respective headlines.

### `sentiment_analysis.py`
This module handles the sentiment analysis of the classified headlines. The function used here analyzes the sentiment of each headline and assigns sentiment scores.

#### Key Function:
- **`analyze_combined_sentiment(data)`**: This function takes in the classified headlines (from `classify_sector`) and analyzes the sentiment using a sentiment analysis model (e.g., Hugging Face’s BERT-based models). It returns a sentiment score along with the probability of positive, neutral, and negative sentiment for each sector on a specific day.

### `adjust_portfolio.py`
The logic in this module adjusts the portfolio weights based on sentiment analysis results. If a sector shows positive sentiment, its weight may increase, and if it shows negative sentiment, its weight may decrease.

#### Key Function:
- **`adjust_portfolio_weights(sentiment_results, portfolio)`**: This function takes the sentiment analysis results and the initial portfolio weights. It adjusts the portfolio weights based on the sentiment of each sector. The higher the positive sentiment, the more weight is assigned to the corresponding sector, while negative sentiment results in a reduced weight. The portfolio is adjusted dynamically for each day’s sentiment.

## Workflow Overview

1. **Fetching News**: The system begins by fetching the latest news for the past `n` days using the `get_past_n_days` function. It then uses the `fetch_broader_market_news` function to collect the headlines for each day.

2. **Classifying Headlines**: Once the headlines are fetched, the `classify_sector` function categorizes them into their respective sectors based on the presence of sector-specific keywords.

3. **Sentiment Analysis**: The `analyze_combined_sentiment` function is used to process the classified headlines. It calculates a sentiment score for each sector, which indicates whether the sentiment is positive, neutral, or negative for the given sector on that day.

4. **Adjusting Portfolio Weights**: Finally, the `adjust_portfolio_weights` function takes the sentiment results and adjusts the portfolio weights accordingly. Positive sentiment increases the weight of a sector, while negative sentiment decreases it.

## Sample Output

The output of the `main.py` script includes:
1. **Sentiment Results**: For each day, sentiment scores are computed for all sectors based on the analyzed headlines.
   
   Example:
   ```python
   Sentiment Results:
   {
       '2025-01-06': {'Energy': {'sentiment_score': 0.1, 'positive_prob': 0.6, 'neutral_prob': 0.3, 'negative_prob': 0.1}},
       '2025-01-07': {'Finance': {'sentiment_score': -0.5, 'positive_prob': 0.2, 'neutral_prob': 0.5, 'negative_prob': 0.3}}
   }

    \item \textbf{NewsAPI}: For providing access to the financial news articles.
    \item \textbf{Hugging Face}: For the pre-trained sentiment analysis models.
\end{itemize}

\end{document}
