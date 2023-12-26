#check the password is uppercase,lowercase or not
password=eval(input('enter a pasword'))
validate={'upper':False,'lower':False,'number':False,'char':False}
if len(password)>=8:
    for char in password:
      if 'A'<=char<='Z':
         validate['upper']=True
      elif 'a'<=char<='z':
         validate['lower']=True
      elif '0'<=char<='9':
         validate['number']=True
      elif char!=' ':
         validate['char']=True
else:
     print('password is invalid')

