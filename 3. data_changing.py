import pandas as pd
df = pd.read_csv("pokemon_data.csv")
#df['Total'] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]

df['Total']= df.iloc[:, 4:10].sum(axis=1)

# df = df.drop(columns=['Total'])
# print(df.head(5))

cols = list(df.columns)
df =df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df[['Name', 'Total', "HP"]][0:5])

