def fname(a):
    if a%2==0:
        return True
    else:
        return False
res=filter(fname,[2,3,4,5,6,7,8,9,10])
print(list(res))

