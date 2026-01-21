#program to print the elements of the list in a single line 
cars = ["BMW", "Porshe", "Audi", "Venue"]
def print_el(list):
    for i in list:
        print(i, end = " ")
print_el(cars)