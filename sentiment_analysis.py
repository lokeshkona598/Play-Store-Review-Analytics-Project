import pandas as pd
from textblob import TextBlob
import os

# Load the scraped reviews
df = pd.read_csv('../data/reviews_raw.csv')

# Function to get sentiment polarity
def get_sentiment(text):
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity
    if polarity > 0.1:
        return 'Positive'
    elif polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis
df['Sentiment'] = df['content'].apply(get_sentiment)

# Save cleaned data
df.to_csv('../data/reviews_with_sentiment.csv', index=False)
print("✅ Sentiment analysis complete. File saved to: data/reviews_with_sentiment.csv")
