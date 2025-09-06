# smartfan_sov.py
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Example dataset (replace with real scraped/API data)
data = [
    {"brand": "Atomberg", "text": "Atomberg smart fan is amazing, saves a lot of energy!", "engagement": 120},
    {"brand": "Crompton", "text": "Crompton fan is okay but noisy compared to Atomberg.", "engagement": 80},
    {"brand": "Havells", "text": "Havells fan app is not working properly.", "engagement": 50},
]

analyzer = SentimentIntensityAnalyzer()

# Compute Weighted Mention Score
for post in data:
    sentiment = analyzer.polarity_scores(post["text"])["compound"]
    s_weight = 1 + sentiment
    wms = 1 * (1 + post["engagement"]) * s_weight
    post["sentiment"] = sentiment
    post["wms"] = wms

df = pd.DataFrame(data)

# Aggregate by brand
brand_scores = df.groupby("brand")["wms"].sum()
total = brand_scores.sum()
sov = (brand_scores / total) * 100

print("Share of Voice (%)")
print(sov.round(2))

print("\nData with Sentiment & WMS")
print(df)
