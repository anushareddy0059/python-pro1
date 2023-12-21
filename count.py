#to count number of vowels present in the string
char=eval(input('enter a string'))
i=0
count=0
while i<len(char):
    if char[i] in "aeiouAEIOU":
        count+=1
    i+=1
print(count)
    