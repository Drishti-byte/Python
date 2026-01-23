#program to convert USD to INR using functions 
def convert(usd):
    inr = usd * 87 #1 USD = 86.58 (approx 87) as of June 2025
    print("The value in Indian rupees is",inr)
a = int(input("Enter the amount of usd money:"))
convert(a)