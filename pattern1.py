rows=int(input('enter no of rows'))
col=int(input('enter no of col'))
for i in range(rows):
    for j in range(col):
        if i==0 or i==rows-1:
            if j==0 or j==col-1:
             print('@',end=' ')
        else:
            print('*',end=' ')
    else:
        
             
                 print(' ',end=' ')
    print()           