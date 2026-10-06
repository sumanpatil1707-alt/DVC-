import pandas as pd

data = pd.read_csv("data/dataset.csv")

print("Dataset loaded successfully")
print("Number of records:", len(data))
print(data.head())