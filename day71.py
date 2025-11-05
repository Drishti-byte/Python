#Program to show table data by connecting MySQL with Python
import pymysql 
try:
    connection = pymysql.connect(host = "localhost", user = "root", password = "Drishti@0710",database = "insurance")
    if connection.open:
        print("Connection to the database established successfully!!!") 
        query = "select * from person"
        cursor = connection.cursor() 
        cursor.execute(query) 
        res = cursor.fetchall()
        for row in res:
            print(row) 
    else:
        print("Error connecting to the database!!!") 
except Exception as e:
    print("Error:", e) 
finally:
    if connection.open:
        connection.close() 