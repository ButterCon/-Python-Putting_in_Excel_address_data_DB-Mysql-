import pymysql
import pandas as pd

db_name = ''

def enter_address_mysql(address):
    print("enter_address_mysql")
    db_name = pymysql.connect(
        user='',
        passwd='{}',
        host='',
        db='',
        charset=''
    )
    cursor = db_name.cursor(pymysql.cursors.DictCursor)

    for i in address:
        sql = '''INSERT INTO '테이블명'(속성1, 속성2, 속성3)
          VALUES ('%s', '%s', '%s');''' % (i[0], i[1], i[2])
        cursor.execute(sql) #INSERT 쿼리 실행
        db_name.commit()    #db에 반영