users = {}
prompt = ''

f= open('users.txt', 'r')
msg = f.read()
users = print(msg)
f.close()

while True:
    prompt = input('Are you registered as a user? Press y or n:')

    if prompt == 'n':
        crtusr = input('Enter desired username:')
        
        if crtusr in users:
            print('Username not available try other name')
        else: 
            crtpswd = input('Create password:') 
            privilage = input('Enter privilage, User or Admin:')
            users[crtusr] = [crtpswd,privilage]
        with open('users.txt','a+') as data:
            data.write(str(users))
    data.close()    
    
