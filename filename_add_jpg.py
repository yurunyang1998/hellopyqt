import pandas as pd

data = pd.read_csv("smoke_test.csv")

for i in range(len(data)):
    temp  = str(data["filename"][i][:-2][3:])
    ten = temp+".jpg"
    data["filename"][i]=ten


data.to_csv('smoke_test.csv', index=None)