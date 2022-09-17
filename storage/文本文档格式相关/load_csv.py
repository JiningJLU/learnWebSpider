import csv
with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


import pandas as pd

df = pd.read_csv('data.csv')
print(df)

data = df.values.tolist()
print(data)

for index, row in df.iterrows():
    print(row.tolist())