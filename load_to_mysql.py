import mysql.connector
import pandas as pd

df = pd.read_csv('../data/redbus_reviews_cleaned.csv')

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Lokesh0598#',
    database='redbus_reviews'
)
cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (userName, content, score, at, thumbsUpCount, sentiment)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
conn.close()
print("✅ Data inserted into MySQL.")
