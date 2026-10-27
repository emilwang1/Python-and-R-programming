import pandas as pd
dataframe = pd.read_csv("ww2_casualties_by_country.csv")
#print(dataframe.sum())
#print(dataframe["Civilian_Deaths"].sum())
print(dataframe.groupby("Side")["Civilian_Deaths"].sum())
print(dataframe.groupby("Side")["Country"].count())