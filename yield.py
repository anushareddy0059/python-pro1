def cal(a,b):
    for var in range(a,b+1):
        yield a**2
        yield b*2
out=cal(5,15)
print(out)
print(type(out))
