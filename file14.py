#program to read a binary file 
import pickle 
f = open("student.dat", "rb") 
try:
    while True:
        data = pickle.load(f) 
        print(data) 
except:
    f.close()