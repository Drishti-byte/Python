#program to update a record in the database 
import pymysql 
try:
    con = pymysql.connect(host = "localhost", user = "root", password = "Drishti@0710", database = "insurance")
    if con.open:
        driverid = int(input("Enter the driverid:"))
        name = input("Enter the updated name:")
        address = input("Enter the updated address:")
        query = "update person set address = %s, name = %s where driverid = %s"
        values = (address, name, driverid)
        cur = con.cursor()
        cur.execute(query, values)  
        con.commit()
        print("Record updated successfully!!")
except Exception as e:
    print("Error:", e)
finally:
    if con.open:
        con.close()