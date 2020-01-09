import pathlib
import pandas

login = False
logindata = pandas.read_csv('root/login.csv')
loginuser = pandas.read.csv('root/users.csv')

if user in logindata['username'].tolist():
    print("\nUsername not available")
if user == "" or password == "" or privilege == "":
    print("\nYou cannot register empty user")
moment = pandas.DataFrame(columns=['username'])
moment['username'] = [user]
moment['password'] = password
if privilege.lower() == 'admin':
    moment['isAdmin'] = 1
else:
    moment['isAdmin'] = 0
logindata = logindata.append(moment)
logindata.to_csv("root/login.csv", index=False)
pathlib.mkdir(pathlib.path.join("data", user))
print("\nRegistered user successfully.")

#login
tmoment = pandas.DataFrame(columns=['username'])
tmoment['username'] = [user]
loginuser = loginuser.append(tmoment)
loginuser.to_csv('root/users.csv', index=False)


if login:
    print("\nAlready logged in")            
if user not in logindata['username'].tolist():
    print("\nUsername not registered")
if password != logindata.loc[logindata['username'] == user, 'password'].iloc[0]:
    print("\nWrong password!")
if user in loginuser['username'].tolist():
    print("\nLogged in from different address")
print("\nLogin completed.")    

try:
    if user in loginuser['username'].tolist():
        usrlist = loginuser['username'].tolist().remove(user)
        loginuser['username'] = usrlist
        loginuser.to_csv("root/users.csv", index=False)
    user = None
    rdindex = {}
    print("\nSigned out")
except KeyError:
    print("\nSigned out")