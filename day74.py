#program to delete a record from the database 
import pymysql 
try:
    con = pymysql.connect(host = "localhost", user = "root", password = "Drishti@0710", database = "insurance")
    if con.open:
        driverid = int(input("Enter the driverid you want to delete:")) 
        query = "delete from person where driverid = %s" 
        value = (driverid) 
        cur = con.cursor() 
        cur.execute(query, value) 
        con.commit() 
        print("Record deleted successfully!!!")
except Exception as e:
    print("Error:", e) 
finally:
    if con.open:
        con.close()