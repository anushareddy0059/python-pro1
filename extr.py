char=eval(input('enter a string'))
i=1
out=''
while i<len(char):
    if '0'<=char[i]<='9':
        out=out+char[i]
    i=i+1
print(out)