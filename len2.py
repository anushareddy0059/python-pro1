#to find the length using for loop
def index(a):
    out=[]
    i=0
    for i in range(0,len(a)):
        if a[i] in 'aeiouAEIOU':
            out=out+[i]
            i=i+1
    return out
out=index('anusha')
print(out)