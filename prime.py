#to check given number is prime or not
num=eval(input('enter a value'))
i=1
temp=False
while i<=(num):
    if num%i==0 and i!=1 and i!=num:
        temp=True
    i=i+1
if not temp:
    print('it is a prime number')
else:
    print('it is not a prime')

     
  