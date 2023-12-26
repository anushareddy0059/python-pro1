import random
captcha=''
while len(captcha)<6:
    captcha+=chr(random.randint(65,90))+chr(random.randint(97,122))+str(random.randint(0,9))
print(captcha)