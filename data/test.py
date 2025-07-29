import pandas as pd
df = pd.read_csv("wiki_movie_plots_deduped.csv")
df  = df.dropna(subset=['Plot','Genre'])
df = df[df['Genre'].str.lower()!= 'unknown']
print(df[['Plot','Genre']].head())
print(f"\nTotal usable rows: {len(df)}")