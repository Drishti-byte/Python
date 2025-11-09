#program to search a record from the database 
import pymysql 
try:
    con = pymysql.connect(host = "localhost", user = "root", password = "Drishti@0710", database = "insurance")
    if con.open:
        driverid = int(input("Enter the driverid you want to search:"))
        query = "select * from person where driverid = %s"
        value = (driverid) 
        cur = con.cursor() 
        cur.execute(query, value) 
        res = cur.fetchone() 
        if res != None:
            print(res)
        else:
            print("No person found with the given driverid")
except Exception as e:
    print("Error:", e)
finally:
    if con.open:
        con.close()