#program to replace some data in the file 
with open("practice.txt","r") as f:
    data = f.read()
    print(data)
new_data = data.replace("Java", "Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)