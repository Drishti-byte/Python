#program to check whether the shopkeeper earns profit or incurs loss 
cp = int(input("Enter the cost price of the product:"))
sp = int(input("Enter the selling price of the product:")) 

if cp > sp:
    print("Loss incured:",cp-sp)
elif sp > cp:
    print("Profit earned:",sp-cp)
else:
    print("No profit no loss")