 #wap to find greatest among three numbers
 num1=eval(input('enter a number'))
num2=eval(input('enter a number'))
num3=eval(input('enter a number'))
if num1>num2 and num1>num3:
    print('it is a greatest number')
elif num2>num3:
    print('it is a greatest number')
else:
    print('it is not a greatest number')