def classify_sector(headlines):
    # Define the sectors and associated keywords
    SECTORS = {
        "Technology": ["technology", "AI", "software", "tech", "cloud", "internet", "gadgets"],
        "Energy": ["oil", "energy", "gas", "renewables", "electricity", "solar", "wind", "EIA", "OPEC"],
        "Healthcare": ["health", "pharma", "medicine", "biotech", "hospital", "clinical", "drug"],
        "Finance": ["finance", "banking", "stocks", "bonds", "ETF", "interest rates", "financial market"],
        "Geopolitical": ["geopolitics", "trade", "war", "tension", "policy", "elections", "diplomacy"],
    }
    
    sector_classification = {}
    for sector, keywords in SECTORS.items():
        sector_headlines = [headline for headline in headlines if any(keyword in headline.lower() for keyword in keywords)]
        if sector_headlines:
            sector_classification[sector] = sector_headlines
    
    return sector_classification
