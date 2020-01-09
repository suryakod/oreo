import pathlib
import pandas

login = False
logindata = pandas.read_csv('root/login.csv')


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
logindata = logindata.append(temp)
logindata.to_csv("root/login.csv", index=False)
loaddata()
pathlib.mkdir(pathlib.path.join("data", user))
print("\nRegistered user successfully.")


if login:
    print("\nAlready logged in")            
if user not in logindata['username'].tolist():
    print("\nUsername not registered")
if password != logindata.loc[slogin_session_data['username'] == user, 'password'].iloc[0])
    print("\nWrong password!")

