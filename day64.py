#program to create a contact book using binary files 
import pickle 
import os 

def addContact():
    name = input("Enter name:") 
    phone = input("Enter phone number:") 
    data = [name, phone] 
    f = open("contact.dat", "ab") 
    pickle.dump(data, f) 
    f.close() 
    print("Contact added successfully!!!") 
    
def display():
    f = open("contact.dat", "rb") 
    print("-"*30)
    print("Name\t\tContact") 
    try: 
        while True:
            data = pickle.load(f)
            print(data[0],"\t\t", data[1]) 
    except:
        f.close()
        
def search():
    name = input("Enter the name you want to search:") 
    f = open("contact.dat", "rb") 
    print("-"*30) 
    n = 0
    print("Name\t\tContact") 
    try:
        while True:
            data = pickle.load(f) 
            if data[0] == name:
                print(data[0],"\t\t",data[1]) 
                n += 1 
    except:
        if n == 0:
            print("No such contact found!!") 
        f.close()

def update():
    name = input("Enter the name to be updated:") 
    f = open("contact.dat", "rb") 
    g = open("temp.dat", "wb")
    print("-"*30) 
    n = 0
    print("Name\t\tContact") 
    try:
        while True:
            data = pickle.load(f) 
            if data[0] == name: 
                print(data[0],"\t\t",data[1]) 
                phone = input("Enter the modified phone number:") 
                data[1] = phone 
                n += 1 
            pickle.dump(data, g)
    except:
        f.close()
        g.close()
        if n == 0:
            print("No such contact found!!")
        else:
            os.remove("contact.dat") 
            os.rename("temp.dat", "contact.dat")

def delete():
    name = input("Enter the name to be deleted:") 
    f = open("contact.dat", "rb") 
    g = open("temp.dat", "wb")
    print("-"*40) 
    n = 0 
    try:
        while True:
            data = pickle.load(f) 
            if data[0] == name:
                print("Deleted record:",data[0],"\t\t",data[1]) 
                n += 1
            else:
                pickle.dump(data, g)
    except:
        f.close() 
        g.close() 
        if n == 0:
            print("No such contact found!!")
        else:
            os.remove("contact.dat") 
            os.rename("temp.dat", "contact.dat")
        
while True:
    print("-"*30)
    print("Press 1 - Add a new contact")
    print("Press 2 - Display all contacts")
    print("Press 3 - Search a contact")
    print("Press 4 - Update a contact")
    print("Press 5 - Delete a contact")
    print("Press any other number to exit")
    choice = int(input("Enter your choice:")) 
    if choice == 1:
        addContact() 
    elif choice == 2:
        display() 
    elif choice == 3:
        search() 
    elif choice == 4:
        update() 
    elif choice == 5:
        delete() 
    else: 
        break 