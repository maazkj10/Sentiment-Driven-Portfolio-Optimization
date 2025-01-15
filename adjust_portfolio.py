def adjust_portfolio_weights(sentiment_results, portfolio):
    adjusted_weights = portfolio.copy()

    # Define thresholds for sentiment
    neutral_threshold = 1e-5  # Sentiment scores close to this will be considered neutral
    max_adjustment = 0.1  # Max adjustment for any sector

    # Loop through sentiment results
    for day, sectors in sentiment_results.items():
        for sector, sentiment in sectors.items():
            sentiment_score = sentiment.get('sentiment_score', 0)

            # Adjust weight based on sentiment score
            if abs(sentiment_score) > neutral_threshold:
                if sentiment_score > 0:
                    adjustment = min(max_adjustment, 0.05 * sentiment_score)  # Increase weight for positive sentiment
                elif sentiment_score < 0:
                    adjustment = max(-max_adjustment, 0.05 * sentiment_score)  # Decrease weight for negative sentiment

                # Apply the adjustment to the portfolio
                adjusted_weights[sector] += adjustment

            # Ensure weights are within the 0-1 range
            adjusted_weights[sector] = max(0, min(1, adjusted_weights[sector]))

    # Normalize portfolio weights to sum to 1
    total_weight = sum(adjusted_weights.values())
    for sector in adjusted_weights:
        adjusted_weights[sector] /= total_weight

    return adjusted_weights
