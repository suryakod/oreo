import pathlib
import pandas

class User:
    userId = ""
    
    privilage = ""
    path = ""
    addr = ()


    def __init__(self,path,addr):
        self.path = path
        self._addr = addr
        self.userId = None
        self.is_login = False
        #self.login_session_data = None
        self.logged_users = None
        #self.load_session_data()
        self.client_directory = None
        self.read_file_index = {}
        self.char_count = 100

    def register(self,userId,psw,privilage):
       
        logindata = pandas.read_csv('root/login.csv')

        if user in logindata['username'].tolist():
            print("\nUsername not available")
        if user == "" or psw == "" or privilege == "":
        print("\nYou cannot register empty user")
        moment = pandas.DataFrame(columns=['username'])
        moment['username'] = [userId]
        moment['password'] = psw
        if privilege.lower() == 'admin':
            moment['isAdmin'] = 1
        else:
            moment['isAdmin'] = 0
        logindata = logindata.append(temp)
        logindata.to_csv("root/login.csv", index=False)
        loaddata()
        pathlib.mkdir(pathlib.path.join("data", user))
        print("\nRegistered user successfully.")



    
    def login(self,userId,psw):
        

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

