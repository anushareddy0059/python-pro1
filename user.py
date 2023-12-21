#to know the username and password are valid or not
user={'username':'anu','password':12345}
username=eval(input('enter username:'))
password=eval(input('enter password:'))
if username !=user['username']:
    print('username is invalid')
else:
    print('username is valid')  
 if password !=user['password']:
    print('password is incorrect')
else:
     print('password is valid') 

    
