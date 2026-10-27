import pandas as pd
dataframe = pd.read_csv("ww2_casualties_by_country.csv", index_col = "Country")
print(dataframe[dataframe["Military_Deaths"] > 1000000].to_string())