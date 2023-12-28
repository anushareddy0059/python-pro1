def lower(a):
    if 'a'<=a<='z':
        return True
    else:
        return False
def ascii(a):
    return ord(a)
res=map(ascii,filter(lower,'a1b2c3Def12@#9Z'))
print(list(res))