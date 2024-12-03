import pandas as pd
import re


df = pd.read_csv("Modified.csv")

# new_df = df.loc[(df['HP'] >= 80) & (df['Type 1'] == 'Grass') & (df['Speed'] >= 100)]


""" for resetting the index of filtered data
& inplace is used for saving changing in variable without assigning"""
# new_df.reset_index(drop=True, inplace=True)


""" if we use lower case words which  declared in Capital words in csv file , 
it will show Empty dataframe  we can avoid that by using  flag =re.I"""

var1 = df.loc[df['Type 1'].str.contains('fire', flags=re.I, regex=True)]

#var = df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)]
print(var1)
