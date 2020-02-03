import psycopg2
import sys
import csv

con = None

try:
    con = psycopg2.connect("host='HOSTNAME' dbname='DBNAME' user='USERNAME' password='PASSWORD'")  
    print("> DB Connection estabilished");
    cur = con.cursor()
    cur.execute("select * from TABLE_NAME;")
    with open('user.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['COLUMN_NAME_1', 'COLUMN_NAME_2'])

        while True:
            row = cur.fetchone()
            if row == None:
                break

            writer.writerow([row[0], row[1]])
except e:
    if con:
        con.rollback()
    
    print('Error', e)    
    sys.exit(1)
finally:   
    if con:
        con.close()
        print("> DB Connection ended");
