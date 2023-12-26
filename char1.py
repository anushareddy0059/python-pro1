#to count the characters
def count_chr(a,ch):
    count=0
    for i in a:
        if i==ch:
            count+=1
    return count
c=count_chr('anusha','a')
print(c)
