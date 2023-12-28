a='ABCDEF'
out=''
c=enumerate(a)
d={j:i for i,j in enumerate(a) if(i%2==0)}
print(d)