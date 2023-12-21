#wap to find the grade of a student based on percentage
marks=eval(input('enter marks'))
if (marks<100 and marks>=90):
    print('A+ grade')
elif(marks<90 and marks>=80):
    print('A grade')
elif(marks<80 and marks>=70):
    print('B grade')
elif(marks<70 and marks>=60):
 print('C grade')
elif(marks<60 and marks>=35):
    print('pass')
elif(marks<0 and marks>35):
    print('fail')
else:
    print('')

