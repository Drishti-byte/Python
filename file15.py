#program to create a menu driven program 
import pickle 
print("------------------------------------- MENU ------------------------------------") 
print("Press 1 - Add a new student") 
print("Press 2 - Display the file") 
print("Press 3 - Display only scholars") 
print("Press 4 - Search a student") 
print("Press 5 - Exit") 
choice = int(input("Enter your choice:")) 
if choice == 1:
    f = open("student.dat", "ab")
    sid = int(input("Enter student roll no:")) 
    sname = input("Enter name:") 
    marks = int(input("Enter marks:"))
    stu = [sid, sname, marks] 
    data = pickle.dump(stu, f) 
    f.close()
elif choice == 2:
    f = open("student.dat", "rb") 
    try: 
        while True:
            data = pickle.load(f)
            print(data) 
    except:
        f.close()
elif choice == 3:
    f = open("student.dat", "rb") 
    try: 
        while True:
            data = pickle.load(f) 
            if data[2] >= 80:
                print(data) 
    except:
        f.close() 
elif choice == 4:
    f = open("student.dat", "rb") 
    roll = int(input("Enter the roll no of the student you want to search:"))
    try: 
        while True:
            data = pickle.load(f) 
            if roll in data[0]:
                print("Student found !!!")
                print(data)
            else: 
                print("Student not found !!!")
    except:
        f.close()
elif choice == 5:
    print("Exiting the program............") 
    exit() 
else:
    print("Please enter a valid option !!!")