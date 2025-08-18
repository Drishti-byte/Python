#program to calculate the shopping bill with gst
name = input("Enter the customer's name:")
cost = float(input("Enter the cost of the product:"))
qty = int(input("Enter the quantity:"))
amount = cost * qty 
gst = 12 * amount / 100
total = amount + gst 
if total < 1000:
    discount = 0 
elif total >= 1000 and total < 3000:
    discount = 0.1 * total 
else:
    discount = 0.2 * total
print("-"*40)
print("Customer Name:",name)
print("Amount:",amount)
print("GST(12%):",gst)
print("Discount:",round(discount, 2))
print("Total amount to be paid:",total - discount)
print("-"*40)