import pandas as pd
#pokemon_df_csv = pd.read_csv("pokemon_data.csv")
#pokemon_df_xlsx = pd.read_("pokemon_data.xlsx")
pokemon_df_txt = pd.read_csv("pokemon_data.txt", delimiter="\t")

print(pokemon_df_txt.head(3))

