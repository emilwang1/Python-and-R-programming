import pandas as pd
data = {"Emil" : [99, 99, 100, 40, 50], "Daniel" : [80, 80, 99, 90, 90]}
dataframe = pd.DataFrame(data, index = ["Rating 1", "Rating 2", "Rating 3", "Rating 4", "Rating 5"])
print(dataframe)
print(dataframe.loc["Rating 1"])
dataframe["Danica"] = [200, 200, 200, 200, 200]
print(dataframe)
new_row = pd.DataFrame([{"Emil": 100, "Daniel": 100, "Danica": 500}], index = ["Rating 6"])
dataframe = pd.concat([dataframe, new_row])
print(dataframe)