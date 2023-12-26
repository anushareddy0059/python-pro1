#to generate a otp
import random

otp=''
while len(otp)<4:
    otp+=str(random.randint(0,9))
print(otp)
