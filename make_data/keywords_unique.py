
import pandas as pd

df = pd.read_json('keyword_model.json')
print(df['pk'].nunique())