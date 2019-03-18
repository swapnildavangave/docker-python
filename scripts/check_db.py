#!/usr/bin/python3

# from configuartions import db_configs
import pymysql as pml
db_configs = {'user':'user','password':'password','host':'mysqlserver','port':3306}
import time

if __name__ == '__main__':

    while True:
        try:
            conn = pml.connect()
        except Exception as e:
            print("connection exception: ")
            print("cause:",str(e))
            continue
        try:
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES;")
            print("DATABASES: ")
            for row in cursor.fetchall():
                print(row)
        except Exception:
            print("query execution exception: ")
            print("cause:",str(e))
        
        finally:
            conn.close()

        time.sleep(30)