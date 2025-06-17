import mysql.connector
import pandas as pd

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lokesh0598#",  # Replace with your password
    database="playstore_reviews"
)

# Read table
df = pd.read_sql("SELECT * FROM reviews", conn)

# Export to CSV
df.to_csv("../data/reviews_for_powerbi.csv", index=False)

print("✅ Exported reviews_for_powerbi.csv successfully!")

conn.close()
