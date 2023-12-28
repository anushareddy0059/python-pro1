print("welcome to book my show")
name=input('enter your name')
seat=eval(input('select number of seats:-'))
print('enter 1 to select diamond')
print('enter 2 to select gold')
print('enter 3 to select silver')
type=(int(input('enter the type of seat what you want')))
if(type==1):
    print('it is a diamond and the cost is 200')
    cost=200
elif(type==2):
    print('it is a gold and the cost is 150')
    cost=150
elif(type==3):
    print('it is gold and the cost is 100')
    cost=100
else:
    print('invalid seat')
   
print('welcome to book my show',name)
print('you booked the seats',seat)
print('you have selected type',type,'and the amount is',seat*cost )

