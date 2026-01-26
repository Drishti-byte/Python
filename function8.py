#program to use *args and *kwargs 
# def greet(name, msg):
#     print(f"{msg}, {name}!!!")
# greet("Alice","Hello")

#multiplying numbers using *args 
# def multiply(*args):
#     product = 1 
#     for i in args:
#         product *= i 
#     return product
# print("The product is:",multiply(10, 15, 78))

#use of *kwargs (key-value pairs) 
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, "=", val)
fun(s1 = "I", s2 = "am", s3 = "learning", s4 = "Python")    