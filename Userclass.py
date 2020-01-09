import pathlib
import pandas

class User:
    def __init__(self,path,addr):
        self.path = path
        self._addr = addr
        self.userId = None
        self.is_login = False
        self.loginusers = None
        self.logged_users = None
        #self.load_session_data()
        self.client_directory = None
        self.rdindex = {}
        self.char_count = 100

    def register(self,userId,psw,privilege):
       
        logindata = pandas.read_csv('root/login.csv')

        if userId in logindata['username'].tolist():
            print("\nUsername not available")
        if userId == "" or psw == "" or privilege == "":
            print("\nYou cannot register empty user")
        moment = pandas.DataFrame(columns=['username'])
        moment['username'] = [userId]
        moment['password'] = psw
        if privilege.lower() == 'admin':
            moment['isAdmin'] = 1
        else:
            moment['isAdmin'] = 0
        logindata = logindata.append(moment)
        logindata.to_csv("ServerAccessSession/Users.csv", index=False)
        pathlib.Path.mkdir(pathlib.Path.join("data", self.userId))
        print("\nRegistered user successfully.")



    
    def login(self,userId,psw):

        login = False
        logindata = pandas.read_csv('root/login.csv')
        loginuser = pandas.read.csv('root/users.csv')
        
        tmoment = pandas.DataFrame(columns=['username'])
        tmoment['username'] = [userId]
        loginuser = loginuser.append(tmoment)
        loginuser.to_csv('root/users.csv', index=False)


        if self.islogin:
            print("\nAlready logged in")            
        if userId not in logindata['username'].tolist():
            print("\nUsername not registered")
        if psw != logindata.loc[logindata['username'] == userId, 'password'].iloc[0]:
            print("\nWrong password!")
        if userId in loginuser['username'].tolist():
            print("\nLogged in from different address")
        print("\nLogin completed.")    

        
    def logout(self):

        self.loginuser = pandas.read.csv('root/users.csv')
        try:
            if self.userId in loginuser['username'].tolist():
                usrlist = loginuser['username'].tolist().remove(user)
                loginuser['username'] = usrlist
                loginuser.to_csv("root/users.csv", index=False)
            user = None
            self.rdindex = {}
            print("\nSigned out")
        except KeyError:
            print("\nSigned out")



    def delete(self,userId,pws):
        pass

    def change_folder(self,path):
        pass

    def list(self,path):
        pass

    def read_file(self,path):
        pass

    def write_file(self,path):
        pass

    def create_folder(self,path):
        pass

