import pymysql
import pandas as pd

def enter_address_mysql(address):
    try:
        print("db연결중...")
        test = pymysql.connect(
            user='root',
            passwd='1234',
            host='127.0.0.1',
            port='3306',
            db='test',
            charset='utf8'
        )
        sql = "INSERT INTO ADDRESS(city_nm, borough_nm, dong_nm) VALUES (%s, %s, %s)"
        data = [tuple(x) for x in address]

        conn = pymysql.connect()

        try:
            with conn.cursor() as cursor:
                cursor.executemany(sql, data)
                conn.commit()

        finally:
            conn.close()
    except:
        print("db연결 실패")

# def enter_address_mysql(address):
#     print("enter_address_mysql")
#
#     test = pymysql.connect(
#         user='root',
#         passwd='{dbdl4fkd!}',
#         host='127.0.0.1',
#         db='test',
#         charset='utf8'
#     )
#     cursor = test.cursor(pymysql.cursors.DictCursor)
#
#     for i in address:
#         sql = '''INSERT INTO 'ADDRESS'(city_nm, borough_nm, dong_nm)
#              VALUES ('%s', '%s', '%s');''' % (i[0], i[1], i[2])
#         cursor.execute(sql)  # INSERT 쿼리 실행
#         test.commit()  # db에 반영
#
#     # for i in address:
#     #     sql = '''INSERT INTO 'CITY_CODE'(city_nm)
#     #       VALUES ('%s');''' % (i[0])
#     #     cursor.execute(sql) #INSERT 쿼리 실행
#     #     db_name.commit()    #db에 반영
#     #
#     #     sql = '''INSERT INTO 'BOROUGH_CODE'(borough_nm)
#     #       VALUES ('%s');''' % (i[1])
#     #     cursor.execute(sql) #INSERT 쿼리 실행
#     #     db_name.commit()    #db에 반영
#     #
#     #     sql = '''INSERT INTO 'DONG_CODE'(dong_nm)
#     #       VALUES ('%s');''' % (i[2])
#     #     cursor.execute(sql) #INSERT 쿼리 실행
#     #     db_name.commit()    #db에 반영
