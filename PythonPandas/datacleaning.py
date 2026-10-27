import pandas as pd
dataframe = pd.read_csv("ww2_casualties_by_country.csv")
dataframe = dataframe.drop(columns=["Population_1939", "Casualties_Pct_Population"])
#print(dataframe)
dataframe = dataframe["Country"].replace({"Germany" : "Nazi Germany"})
print(dataframe)