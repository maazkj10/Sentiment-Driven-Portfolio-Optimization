from transformers import BertTokenizer, BertForSequenceClassification
import torch

def analyze_combined_sentiment(daily_headlines):
    model_name = 'yiyanghkust/finbert-tone'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=3)
    
    sentiment_results = {}
    
    for date, headlines in daily_headlines.items():
        combined_text = " ".join(headlines)  # Combine all headlines into one string
        inputs = tokenizer(combined_text, return_tensors="pt", truncation=True, padding=True)
        
        # Sentiment prediction
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            probabilities = torch.softmax(logits, dim=-1).squeeze().cpu().numpy()
        
        positive_prob, neutral_prob, negative_prob = probabilities
        sentiment_score = positive_prob - negative_prob
        
        sentiment_results[date] = {
            'sentiment_score': sentiment_score,
            'positive_prob': positive_prob,
            'neutral_prob': neutral_prob,
            'negative_prob': negative_prob
        }
    
    return sentiment_results
