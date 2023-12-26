#to check the password is valid or not
password=eval(input('enter a pasword'))
validate={'upper':False,'lower':False,'number':False,'char':False,'space':False,}
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
      elif char==' ':
         validate['space']=True
         break
    if(validate['upper'] and validate['lower'] and validate['number'] and validate['char'] and not validate['space']):
      print('password is correct')
    else:
      print('password is invalid')
else:
     print('password is invalid')
