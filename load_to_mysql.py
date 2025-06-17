import pandas as pd
import mysql.connector

# Load data with sentiment
df = pd.read_csv('../data/reviews_with_sentiment.csv')

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lokesh0598#',  # Replace with your password
    database='playstore_reviews'
)
cursor = conn.cursor()

# Insert rows
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (userName, score, content, reviewDate, thumbsUpCount, sentiment)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row['userName'],
        int(row['score']),
        row['content'],
        row['at'],
        int(row['thumbsUpCount']),
        row['Sentiment']
    ))

conn.commit()
cursor.close()
conn.close()

print("✅ Data successfully loaded into MySQL table 'reviews'")
