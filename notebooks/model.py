import pandas as pd

train = pd.read_csv("../data/train.csv")
test = pd.read_csv("../data/test.csv")

print("train:", train.shape)
print("test :", test.shape)

print(train.head())

print(train.info())

print(train.columns)