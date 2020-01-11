import pathlib
import pandas

class User:
    def __init__(self,path,addr):
        self.path = path
        self._addr = addr
        self.userId = None
        self.islogin = False
        self.loginusers = None
        self.logged_users = None
        #self.load_session_data()
        self.client_directory = None
        self.rdindex = {}
        self.char_count = 100

    def register(self,userId,psw,privilege):
       
        logindata = pandas.read_csv('ServerAccessSession/Users.csv')

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
        directoryname = str(self.userId)
        if(moment['isAdmin']==1):
            filepath = "GitHub/oreo/Root/Admin/" + directoryname
        else:
            filepath = "GitHub/oreo/Root/NotAdmin/" + directoryname
        pathlib.Path(filepath).mkdir(parents=True,exist_ok=True)
        #pathlib.Path.join("data", self.userId)
        print("\nRegistered user successfully.")

   
    def login(self,userId,psw):

        #self.islogin = False
        logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        loginuser = pandas.read.csv('ServerAccessSession/logged_in_Users.csv')
        

        if self.islogin:
            print("\nAlready logged in")            
        if userId not in logindata['username'].tolist():
            print("\nUsername not registered")
        if psw != logindata.loc[logindata['username'] == userId, 'password'].iloc[0]:
            print("\nWrong password!")
        if userId in loginuser['username'].tolist():
            print("\nLogged in from different address")

        self.is_login = True
        self.username = userId
        self.client_directory = ""
        tmoment = pandas.DataFrame(columns=['username'])
        tmoment['username'] = [userId]
        loginuser = loginuser.append(tmoment)
        loginuser.to_csv('ServerAccessSession/logged_in_Users.csv', index=False)
        
        print("\nLogin completed.")    

        
    def quit(self):

        loginuser = pandas.read.csv('ServerAccessSession/logged_in_Users.csv')
        try:
            if self.userId in loginuser['username'].tolist():
                usrlist = loginuser['username'].tolist().remove(self.userId)
                loginuser['username'] = usrlist
                loginuser.to_csv('ServerAccessSession/logged_in_Users.csv', index=False)
            self.userId = None
            self.client_directory= ""
            self.islogin = False
            self.rdindex = {}
            print("\nSigned out")
        except KeyError:
            print("\nSigned out")



    def delete(self,userId,pws):
        pass

    def change_folder(self,directory):
        
        if not self.islogin:
            return "\nLogin to continue"
        n = int(self.loginusers.loc[self.login_session_data['username'] == username, 'isAdmin'].iloc[0])
        if (n==1):
            path = pathlib.Path("/Root/Admin/")
        else:
            path = pathlib.Path("/Root/NotAdmin/")
        path = path/str(self.userId)
        totaldir = [e for e in path.iterdir() if e.is_dir()]
        path_change = pathlib.PurePath(path).joinpath(self.client_directory,directory)
        if path_change in totaldir:
            self.client_directory = pathlib.PurePath().joinpath(self.client_directory,directory)
            return "\n changed directory to "+directory+"successful"
        return"\nInput correct directory name"

        
    def list(self):
        if not self.islogin:
            return "\nLogin to continue!!"
        p = int(self.loginusers.loc[self.loginusers['username'] == self.userId, 'isAdmin'].iloc[0])
        if(p==1):
            path = pathlib.PurePath("/Root/Admin/").joinpath(str(self.userId),self.client_directory)
        else:
            path = pathlib.PurePath("/Root/NotAdmin/").joinpath(str(self.userId),self.client_directory)
        totaldir = []
        for file_name in path.iterdir():
            totaldir.append([str(file_name),str(file_name.stat().st_size),str(file_name.stat().st_mtime)])
        response = "\nFile|Size|Modified Date"
        for data in totaldir:
            oneline = " | ".join([data[0],data[1],data[2]]) + "\n"
            response += "-------\n" + oneline
        return response


    def read_file(self,path):
        pass

    def write_file(self,path):
        if not self.islogin:
            return "\nLogin to continue!!"
        p = int(self.loginusers.loc[self.loginusers['username'] == self.userId, 'isAdmin'].iloc[0])
        if(p==1):
            path1 = pathlib.PurePath("/Root/Admin/").joinpath(str(self.userId),self.client_directory,path)
        else:
            path1 = pathlib.PurePath("/Root/NotAdmin/").joinpath(str(self.userId),self.client_directory,path)
        t_file = []
        for fil in pathlib.Path(path1).iterdir():
            p = pathlib.Path(path1)/fil
            if p.is_file:
                t_file.append(fil)
        if(path in t_file):
            with open(path1, "a+") as file:
                msg = input("user input")
                file.write(msg)
            file.close()
            return"\nSuccess written"
        with open(t_file, "w+") as file:
            msg = input("user input")
            file.write(msg)
        file.close()
        return"\nSuccessfully written"
    
    
    
    def create_folder(self,path):
        if not self.islogin:
            return"\nLogin to Continue"
        p = int(self.loginusers.loc[self.login_session_data['username'] == username, 'isAdmin'].iloc[0])
        if(p==1):
            curr_dir = pathlib.Path("/Root/Admin/")
        else:
            curr_dir = pathlib.Path("/Root/NotAdmin/")
        path1 = pathlib.PurePath(curr_dir).joinpath(str(self.userId),self.client_directory)
        total_avail_dir = []
        for sub in pathlib.Path(path1).iterdir():
            if (sub.is_dir(pathlib.PurePath.joinpath(path1,sub))):
                total_avail_dir.append(sub)
        if path in total_avail_dir:
            return "\nThis directory is already created"
        pathlib.Path(path1).mkdir(parents=True,exist_ok=True)
        return"\nSuccess"

