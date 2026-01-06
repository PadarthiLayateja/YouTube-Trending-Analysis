# preprocess_youtube.py

import pandas as pd
import re
from sklearn.preprocessing import MinMaxScaler

# === 1. Load the dataset ===
print("Loading data...")
df = pd.read_csv("youtube_trending.csv", encoding='utf-8')
print("Data loaded successfully!\n")

# === 2. Check basic info ===
print("Initial shape:", df.shape)
print("\nChecking for missing values...\n")
print(df.isnull().sum())

# === 3. Drop duplicates and missing rows ===
df = df.drop_duplicates()
df = df.dropna(subset=['title'])   # 'description' not present in this dataset

# === 4. Clean text columns ===
def clean_text(text):
    text = re.sub(r"http\S+", "", str(text))       # remove URLs
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)     # remove special characters
    text = text.lower().strip()
    return text

print("\nCleaning text columns...")
df['title'] = df['title'].apply(clean_text)
df['channel_title'] = df['channel_title'].apply(clean_text)

# === 5. Convert date columns ===
date_cols = ['publish_time', 'trending_date']
for col in date_cols:
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')

# === 6. Normalize numeric columns ===
numeric_cols = ['views', 'likes', 'comments']   # correct column names
existing_numeric = [col for col in numeric_cols if col in df.columns]

if existing_numeric:
    print("\nNormalizing numeric columns:", existing_numeric)
    scaler = MinMaxScaler()
    df[existing_numeric] = scaler.fit_transform(df[existing_numeric])

# === 7. Save cleaned file ===
df.to_csv("youtube_trending_cleaned.csv", index=False, encoding='utf-8')
print("\n✅ Preprocessing completed successfully!")
print("Cleaned data saved as 'youtube_trending_cleaned.csv'")
print("Final shape:", df.shape)
