import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])
    writer.writerows([['10004', 'Jack', 23], ['10005', 'Yoyo', 24]])

with open('data_map.csv', 'w') as csvfile2:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

import pandas as pd

data = [
    {'id': '10001', 'name': 'Mike', 'age': 20},
    {'id': '10002', 'name': 'Bob', 'age': 22},
    {'id': '10003', 'name': 'Jordan', 'age': 21}
]

dataFrame = pd.DataFrame(data)
dataFrame.to_csv('data_pandas.csv', index=False)