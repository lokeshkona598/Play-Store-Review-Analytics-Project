# 📱 Play Store Review Analytics Dashboard

Analyze user reviews of a Play Store app using **Python**, **MySQL**, and **Power BI** to gain insights from real user sentiment and ratings.

---

## 📊 Project Overview

This project collects and analyzes user reviews of the **Instagram** app from the Google Play Store. It uses sentiment analysis to categorize reviews as Positive, Negative, or Neutral and visualizes the results in an interactive Power BI dashboard.

---

## 🛠️ Tech Stack

- **Python**: Data scraping, cleaning, sentiment analysis
- **MySQL**: Structured storage of review data
- **Power BI**: Data visualization and dashboard creation
- **Google Play Scraper**: Library to extract app reviews

---

## 🗂️ Project Structure

playstore_review_project/
├── data/ ← Raw & cleaned review CSV files
├── scripts/ ← Python scripts for scraping & NLP
├── db/ ← SQL schema & setup files
├── powerbi/ ← Power BI dashboard (.pbix)
├── README.md ← Project documentation

---

## 📌 How It Works

### 1. **Scrape Reviews**
- Tool: `google-play-scraper`
- Output: `whatsup_reviews_raw.csv`

### 2. **Preprocess & Analyze**
- Clean data using `pandas`
- Perform sentiment analysis with `TextBlob`
- Export as `whatsup_reviews_cleaned.csv`

### 3. **Load into MySQL**
- Use `schema.sql` to create database & table
- Insert cleaned data into `playstore_reviews.reviews`

### 4. **Visualize in Power BI**
- Connect Power BI to MySQL
- Create visuals:
  - Sentiment distribution
  - Rating breakdown
  - Word cloud
  - Review trends

---

## 📎 Sample Visuals


![image](https://github.com/user-attachments/assets/8258ad08-7d0c-475e-a40c-afbca10ed30e)

---

## ⚙️ Setup Instructions

### Requirements:
- Python 3.x
- MySQL Server
- Power BI Desktop (Windows)
- pip packages: `google-play-scraper`, `pandas`, `textblob`, `mysql-connector-python`

### To Run:
```bash
# Install required packages
pip install google-play-scraper pandas textblob mysql-connector-python

# Run script to scrape and clean data
python scripts/scrape_reviews.py
python scripts/sentiment_analysis.py

# Load data to MySQL
python scripts/load_to_mysql.py
