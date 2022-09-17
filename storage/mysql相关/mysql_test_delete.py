import pymysql

db = pymysql.connect(host='localhost', user='root', password='980909', port=3306, db='spiders')
cursor = db.cursor()

table = 'students'
condition = 'age > 20'

sql = f'DELETE FROM {table} WHERE {condition}'
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
