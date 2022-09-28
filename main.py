import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')
print(df)

print(df.columns)

print(df.drop)

final_data = df.dropna()
print(final_data)

final_data.reset_index(drop=True,inplace = True)
print(final_data)