import pandas as pd

df = pd.read_json('movie_model.json')
print(df['pk'].nunique())