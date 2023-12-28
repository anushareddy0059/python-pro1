def mul(a):
    if a%2==1:
        return a, a**2
    else:
        return False
res=map(mul,range(1,101))
print(list(res))