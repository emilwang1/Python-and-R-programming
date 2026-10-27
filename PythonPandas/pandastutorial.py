import pandas as pd

data = [101, 102, 103]

series = pd.Series(data, index = ["a", "b", "c"])

print(series)
print(series["a"])
series["a"] = 9000
print(series)
print(series.iloc[1])
print(series[series >= 200])