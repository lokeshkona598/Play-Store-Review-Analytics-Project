from google_play_scraper import reviews, Sort
import pandas as pd
import os
os.makedirs("../data", exist_ok=True)


result, _ = reviews(
    'in.redbus.android',  # Redbus app package
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=1500
)

df = pd.DataFrame(result)
df = df[['userName', 'content', 'score', 'at', 'thumbsUpCount']]
df.to_csv('../data/redbus_reviews_raw.csv', index=False)
print("✅ Scraping complete.")
