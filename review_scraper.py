from google_play_scraper import reviews, Sort
import pandas as pd
import os

# App package name from Play Store (We are Taking WhatsApp)
app_package = 'com.whatsapp'

# Scrape the latest 1000 reviews
result, _ = reviews(
    app_package,
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=1000,
)

# Convert to DataFrame
df = pd.DataFrame(result)

# Select important columns
df = df[['userName', 'score', 'content', 'at', 'thumbsUpCount']]

# Save to CSV
os.makedirs('../data', exist_ok=True)
df.to_csv('../data/reviews_raw.csv', index=False)

print("✅ 1000 reviews saved to: data/reviews_raw.csv")
