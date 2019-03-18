#!/usr/bin/python3

# from configuartions import db_configs
import logging
import pymysql as pml
db_configs = {'user':'user','password':'password','host':'db','port':3306}
import time
logging.basicConfig(filename='/scripts/output.log',level=logging.DEBUG)
if __name__ == '__main__':

    time.sleep(60)
    while True:
        try:
            conn = pml.connect(host=db_configs['host'],user=db_configs['user']
            ,port=db_configs['port'],password=db_configs['password'])
            logging.info("Connection made.")
        except Exception as e:
            print("connection exception: ")
            print("cause:",str(e))
            time.sleep(30)
            logging.warning(str(e))
            continue
        try:
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES;")
            print("DATABASES: ")
            for row in cursor.fetchall():
                print(row)
                logging.info('{}'.format(row))

        except Exception as e:
            logging.warning(str(e))
            print("query execution exception: ")
            print("cause:",str(e))
        
        finally:
            conn.close()
            logging.info("Connection closed.")
        time.sleep(30)
