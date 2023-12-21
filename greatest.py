#to find the second greatest number 
num1=eval(input('enter a number'))
num2=eval(input('enter a number'))
num3=eval(input('enter a number'))
if num1>num2 and num1>num3:
    if num2>num3:
        print(num2,'is the second greatest number')
    else:
        print(num3,'is the second greatest number')
elif num2>num3:
    if num1>num3:
        print(num1,'is the second greatest number')
    else:
        print(num3,'is the second greatest number')
else:
    if num1>num2:
        print(num1,'is the second greatest number')
    else:
        print(num2,'is the second greatest number')
        