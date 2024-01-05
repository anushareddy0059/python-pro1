import re
file=open(r"C:\Users\administrator.MCA\Desktop\New Text Document.txt",'r')
data=file.read()
data1=re.split(' ',data)
count=0
words=[]
for i in data1:
    out=re.match('^a',i)
    if out:
        words+=[i]
        count+=1
print(count)
print(words)
