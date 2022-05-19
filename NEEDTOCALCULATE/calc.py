from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
import pandas as pd

sia = SentimentIntensityAnalyzer()

df = pd.read_csv(r'C:\Users\Rehts\Documents\Repositories\cronos-sentiment-analyse\NEEDTOCALCULATE\givescore.csv')

results = {}
results = {}
for i, row in tqdm(df.iterrows(), total=len(df)):
    text = row['opinion']
    my_id = row['id']
    results[my_id] = sia.polarity_scores(text)

vaders = pd.DataFrame(results).T # flipping the dataset
vaders = vaders.reset_index().rename(columns={'index': 'id'})
vaders = vaders.merge(df, how='left')

vaders.to_csv(r'C:\Users\Rehts\Documents\Repositories\cronos-sentiment-analyse\NEEDTOCALCULATE\calculated.csv', index=False, mode='a', header=True)