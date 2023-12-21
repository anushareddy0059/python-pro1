#to find the uppercase and lowercase character
char=(input('enter a character'))
if 'A'<=char <= 'Z':
 print('it is uppercase')
elif 'a'<=char <='z':
 print('it is lowercase')
elif '0' <=char <='9':
    print('it is a digit')
else:
    print('it is a special character')