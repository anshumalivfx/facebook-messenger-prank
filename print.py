import pandas as pd
data = pd.read_csv("list.csv")
print(data.iat[1,0])
for i in range(0,10):
    i += 1
    print(data.iat[i,0])