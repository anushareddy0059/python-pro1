#to find factrorial of a number using recursion
def fact(num,i=1):
    if num==i:
        return i
    return num*fact(num,i+1)
c=fact(3)
print(c)