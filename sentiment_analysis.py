import pandas as pd
from textblob import TextBlob
import os

df = pd.read_csv('../data/redbus_reviews_raw.csv')

def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment'] = df['content'].apply(get_sentiment)
df.to_csv('../data/redbus_reviews_cleaned.csv', index=False)
print("✅ Sentiment analysis complete.")
