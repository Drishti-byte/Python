#program to print the electricity bill 
units = float(input("Enter the units of electricity consumed:"))
if units < 200:
    amount = units * 4
elif units >= 200 and units < 500:
    amount = 800 + (units - 200) * 6
elif units >= 500 and units < 800:
    amount = 800 + 1800 + (units - 500) * 8
else:
    amount = 800 + 1800 + 2400 + (units - 800) * 10
print("Amount to be paid:",amount)