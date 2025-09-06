## ATOMBERG - AI/ML Problem statement repo.

# Smart Fan SoV Agent

This repository contains a prototype AI/ML pipeline to analyze the Share of Voice (SoV) and Share of Positive Voice (POSV) for the keyword “smart fan”, with a focus on Atomberg vs competitors.

# Features
1)Collects search/social data (Google, YouTube, X) – extendable to Instagram/Reddit.
2)Detects brand mentions (Atomberg, Crompton, Havells, Orient, Usha, etc.).
3)Runs sentiment analysis (VADER / Hugging Face).
4)Calculates Weighted Mention Score (WMS) per brand.
5)Outputs Share of Voice (%) and sentiment breakdown.

# Files
1)smartfan_sov.py → minimal prototype (demo dataset + SoV calculation).
2)requirements.txt → dependencies (VADER, pandas).
3)(extend with APIs & scrapers later)

# Tech Stack
1)Python 3.10+
2)pandas → data processing
3)vaderSentiment → sentiment analysis
4)matplotlib/plotly (optional) → visualization

# Usage
1) Clone repo
git clone https://github.com/your-username/smartfan-sov.git
cd smartfan-sov

2) Install dependencies
pip install -r requirements.txt

3) Run prototype
python smartfan_sov.py

# Example Output
1)Share of Voice (%)
2)Atomberg    44.00
3)Crompton    31.00
4)Havells     25.00

# Next Steps
1)Replace demo data with real API data from Google/YouTube/X.
2)Extend to Instagram & Reddit.
3)Add dashboard (Streamlit) for interactive insights.
