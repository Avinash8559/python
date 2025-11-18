# OTP loop

import random

otp =  random.randint(1000,10000)
print(otp)

attempts = 3
while attempts:
    user_otp = int(input("enter otp: "))
    if len(str(user_otp)) != 4:
        print("otp must be 4 digit number only")
    if user_otp == otp:
        print("correct otp - success")
        break
    attempts -=1
else:
    print("max attempts done, try after 24 hours")