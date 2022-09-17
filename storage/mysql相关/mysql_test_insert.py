import pymysql

id = '20120001'
name = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='980909', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values(%s, %s, %s)'
try:
    cursor.execute(sql, (id, name, age))
    db.commit()
except:
    db.rollback()

data = {
    'id': '20120002',
    'name': 'Jack',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
# sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
sql = f'INSERT INTO {table}({keys}) VALUES ({values})'
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
