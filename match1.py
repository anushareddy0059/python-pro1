a=int(input('enter a number:-'))
b=int(input('enter a number:-'))
c=int(input('enter what operation u want:-'))
res=0
match c:
    case 1:
        print('addition')
        res=a+b
    case 2:
        print('substraction')
        res=a-b
    case 3:
        print('multiplication')
        res=a*b
    case 4:
        print('division')
        res=a/b
print(res)

