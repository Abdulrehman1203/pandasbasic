import pandas as pd
df = pd.read_csv("pokemon_data.csv")

df['Total'] = df.iloc[:, 4:10].sum(axis=1)
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df[['Name', 'Total', "HP"]][0:5])

df.to_csv("Modified.csv")
