#program to insert a record in the database 
import pymysql 
try: 
    con = pymysql.connect(host = "localhost", user = "root", password = "Drishti@0710", database = "insurance")
    if con.open:
        driverid = int(input("Enter the driver id:")) 
        name = input("Enter name:") 
        address = input("Enter the address:")
        query = "insert into person values(%s, %s, %s)" 
        values = (driverid, name, address)
        cur = con.cursor()
        cur.execute(query, values) 
        con.commit() 
        print("Record inserted successfully!!")
except Exception as e:  
    print("Error:",e)
finally:
    if con.open:
        con.close()