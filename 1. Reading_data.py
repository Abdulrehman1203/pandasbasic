import pandas as pd
df = pd.read_csv("pokemon_data.csv")

# ------- Reading Headers=====
# print(df.columns)

# ----Reading each column----
# print(df['Name'][0:5])
# print(df[['Name', 'Type 1', "HP"]][0:5])
# print(df.Name)

# ----Reading each Rows----

"""From Top to given index"""
# print(df.head(5))

"""Accessing through index of rows"""
# print(df.iloc[0:4])

""" Accessing the Specific location [R,C])"""
# print(df.iloc[1, 1])
# print(df.iloc[3, 4])

""" Iteration through rows """
# for index, row in df.iterrows():
#    print(index, row['HP'])

""" Accessing rows which have specific properties"""
print(df.loc[df['Type 1'] == "Grass"])
