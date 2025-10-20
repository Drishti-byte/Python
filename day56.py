#program to generate a 4 digit otp
import random 
def generateOtp():
    otp = [] 
    i = 0
    while i < 4:
        digit = random.randint(0, 9) 
        if digit not in otp: 
            otp.append(digit)
            i += 1
    return otp 

otp = generateOtp()
print("Your OTP is:", end = " ") 
for d in otp:
    print(d, end = " ") 