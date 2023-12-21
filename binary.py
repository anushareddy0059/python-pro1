#to toggle the binary numbers 1 and 0
a=input('enter a number')
i=0
out=''
while i<len(a):
    if a[i]=='1':
        out=out+'0'
    else:
        out=out+'1'
    i=i+1
print(out)