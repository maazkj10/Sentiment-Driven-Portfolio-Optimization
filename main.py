from fetch_news import fetch_broader_market_news, get_past_n_days
import classify_sector
from sentiment_analysis import analyze_combined_sentiment
from adjust_portfolio import adjust_portfolio_weights


KEYWORDS = [
    "interest rates", "rate hikes", "rate cuts", "Federal Reserve", 
    "central bank", "monetary policy", "inflation", "quantitative easing",
    "GDP growth", "unemployment rate", "earnings report", "elections",
    "geopolitical tensions", "trade policy", "stock market", "volatility",
    "pandemic", "recession", "energy crisis", "oil prices", "bond yields", "EIA", "OPEC", "IEA"
]

def main():
    # Your API key
    API_KEY = "a592ced6354b46f591769c9ad239dc8a"
    
    # Define sectors and keywords (already defined)
    SECTORS = {
        "Technology": ["technology", "AI", "software", "tech", "cloud", "internet", "gadgets"],
        "Energy": ["oil", "energy", "gas", "renewables", "electricity", "solar", "wind", "EIA", "OPEC"],
        "Healthcare": ["health", "pharma", "medicine", "biotech", "hospital", "clinical", "drug"],
        "Finance": ["finance", "banking", "stocks", "bonds", "ETF", "interest rates", "financial market"],
        "Geopolitical": ["geopolitics", "trade", "war", "tension", "policy", "elections", "diplomacy"],
    }
    
    # Initial portfolio weights
    PORTFOLIO = {
        "Technology": 0.2,
        "Energy": 0.2,
        "Healthcare": 0.2,
        "Finance": 0.2,
        "Geopolitical": 0.2,
    }
    
    # Fetch headlines for the past 10 days
    past_days = get_past_n_days(10)
    daily_headlines = {}
    
    for day in past_days:
        # Fetch news for each day
        from_date = day
        to_date = day
        print(f"Fetching news for {day}...")
        headlines = fetch_broader_market_news(API_KEY, KEYWORDS, from_date, to_date)
        daily_headlines[day] = headlines.get(day, [])
    
    # Classify headlines into sectors
    sector_classification = {}
    for day, headlines in daily_headlines.items():
        print(f"Classifying sectors for {day}...")
        sector_classification[day] = classify_sector.classify_sector(headlines)
    
    # Perform sentiment analysis for each sector
    sentiment_results = {}
    for day, sectors in sector_classification.items():
        day_sentiment = {}
        for sector, headlines in sectors.items():
            sentiment = analyze_combined_sentiment({day: headlines})
            day_sentiment[sector] = sentiment.get(day, {})
        
        # Add the sentiment for this day to the results
        sentiment_results[day] = day_sentiment

    # Print sentiment results for debugging
    print("Sentiment Results:")
    print(sentiment_results)
    
    # Adjust portfolio weights based on sentiment
    print("Adjusting portfolio weights based on sentiment analysis...")
    adjusted_portfolio = adjust_portfolio_weights(sentiment_results, PORTFOLIO)
    
    # Print the adjusted portfolio weights
    print("\nAdjusted Portfolio Weights:")
    for sector, weight in adjusted_portfolio.items():
        print(f"  {sector}: {weight:.2f}")

if __name__ == "__main__":
    main()
