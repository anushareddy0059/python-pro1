def mul(a):
    if a%2==1:
        return True
    else:
        return False
def square(b):
    return b**2
res=map(square,filter(mul,range(1,101)))
print(list(res))