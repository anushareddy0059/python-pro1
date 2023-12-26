#to find the index of the string
def index(a):
    out=[]
    i=0
    while i<len(a):
        if a[i] in 'aeiouAEIOU':
            out=out+[i]
        
        i=i+1
    return out
out=index('happy new year')
print(out)

