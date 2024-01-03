file=open('mca.txt','w')
data='welcome to mca department'
file.write(data)
file.close()

file=open('mca.txt','r')
data=file.read()
print(data)
file.close()
