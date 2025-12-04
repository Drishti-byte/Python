#program to implement data analysis 
import pandas as pd 
stu = {"Rohit" : 90, "Kanak" : 78, "Rahul" : 95, "Garima" : 50, "Pari" : 65}
s = pd.Series(stu)
print(s)
print("Size:",s.size)
print("Nbytes:",s.nbytes)
print(s [ s >= 80])