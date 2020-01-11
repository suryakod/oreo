users = {}
prompt = ''

f= open('file.txt', 'r')
msg = f.read()
users = print(msg)
f.close()



while True:
    prompt = input('Are you registered as a user? Press y or n:')

    if prompt == 'y':
        print('Enter login data')
        usrnme = input('Enter the username:')
        pswd = input('Enter the password:')
        
        if (usrnme in users) and (users[usrnme][0] == pswd):
            print('Login successful')
            if (users[usrnme][1] == 'Admin'):
                print('Your previlage is Admin')
            elif (users[usrnme][1] == 'User'):
                print('Your privilage is User')
        else:
            print('Credentials are wrong')


    if prompt == 'n':
        crtusr = input('Enter desired username:')
        
        if crtusr in users:
            print('Username not available try other name')
        else: 
            crtpswd = input('Create password:') 
            privilage = input('Enter privilage, User or Admin:')
            users[crtusr] = [crtpswd,privilage]
        with open('file.txt','a+') as data:
            data.write(str(users))
    data.close()    
    
