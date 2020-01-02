users = {}
prompt = ''

f= open('users.txt', 'r')
msg = f.read()
users = print(msg)
f.close()


    
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
