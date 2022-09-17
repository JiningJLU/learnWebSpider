import pymysql

db = pymysql.connect(host='localhost', user='root', password='980909', port=3306, db='spiders')
cursor = db.cursor()
sql = 'UPDATE students SET age = %s WHERE name = %s'
try:
    cursor.execute(sql, (25, 'Bob'))
    db.commit()
except:
    db.rollback()

# 上面的做法太简单了，实际上不会这么简单地做的
data = {
    'id': '20120001',
    'name': 'Bob',
    'age': 21
}
table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = f'INSERT INTO {table} ({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update

try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()

db.close()