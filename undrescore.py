char=eval(input('enter a string:-'))
i=0
out=''
while i<len(char):
    if not('A'<=char[i]<='z' or 'a'<=char[i]<='z' or '0'<=char[i]<='a'):
        out=out+'_'
    else:
      out=out+char[i]
    i=i+1
print(out)
    