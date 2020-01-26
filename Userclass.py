'''This program deal with passing commands to the
server from the client
'''

import pathlib
import pandas
import os
from shutil import rmtree 

class User():
    """Used to create a user
    This class involves attributes like
    ------
    self.user_Id : Returns a string representing the user ID of the user
    ------
    self.islogin : Gives data if the user is logged in or not
    ------
    self.loginusers : Returns True if the user is logged in
    ------
    self.loggedusers : Returns a list of users who are already logged in
    ===============
    Methods:
    This class involves methods like:
    ------
    register(): Used to register a new user and enables to create
                a username and password of their choice inorder to
                login.
    ------
    login(): Used to login to the user's account with proper credentials
    ------
    quit(): Represents the Log out of the user from the current login session.
    ------
    change_folder(): Moves the current working directory for the current user to the
                    specified folder residing in the current folder
    ------
    list(): Prints all files and folders in the current working directory for the
            user issuing the request
    ------
    read_file(): Read data from the file <name> in the current working directory for
                the user issuing the request and return the first hundred characters in it.
    ------
    write_file(): Write the data in <input> to the end of the file <name> in the current
                working directory for the user issuing the request, starting on a new line.
    ------
    create_folder(): Create a new folder with the specified <name> in the current working
                    directory for the user issuing the request. """

    def __init__(self):
        '''The parameters are passed to the __init__ function
        The Parameters include :
        ------
        self.user_Id : Returns a string representing the user ID of the user
        ------
        self.islogin : Gives data if the user is logged in or not
        ------
        self.loginusers : Returns True if the user is logged in
        ------
        self.loggedusers : Returns a list of users who are already logged in
        ------'''
        self.user_Id = None
        self.is_login = False
        self.createdusers = None
        self.loggedinusers = None
        self.client_directory = None
        self.rdindex = {}
        self.char_count = 100

    def session(self):
        '''
        This function deals with accessing of user login information
        '''
        self.createdusers = pandas.read_csv("ServerAccessSession/Users.csv")
        self.loggedinusers = pandas.read_csv("ServerAccessSession/logged_in_Users.csv")

    def rm_tree(self, path1):
        '''This function deals with  '''
        for child in pathlib.Path(path1).iterdir():
            if child.is_file():
                child.unlink()
            else:
                self.rm_tree(child)
        path1.rmdir()

    def register(self, user_Id, psw, privilege):
        '''This function is used to create a new user with the privileges
        to the server using the username and password provided.
        --------
        The privileges are either User or Admin.
        --------
        If a username already exists, it displays that the username is not
        available.
        --------
        If no username is entered, it diplays that empty user cannot be registered.'''

        self.session()

        logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        prep = 100
        if user_Id in logindata['username'].tolist():
            return "\nUsername not available"
        if user_Id == "" or psw == "" or privilege == "":
            return "\nYou cannot register empty user"
        moment = pandas.DataFrame(columns=['username'])
        moment['username'] = [user_Id]
        moment['password'] = psw
        if privilege.lower() == 'admin':
            moment['isAdmin'] = 1
            prep = 1
        else:
            moment['isAdmin'] = 0
            prep = 0
        logindata = logindata.append(moment)
        logindata.to_csv("ServerAccessSession/Users.csv", index=False)
        directoryname = str(user_Id)
        if prep == 1:
            filepath = "c:/Users/gvalm/Documents/GitHub/oreo/Root/Admin/"
        else:
            filepath = "c:/Users/gvalm/Documents/GitHub/oreo/Root/NotAdmin/"
        #pathlib.Path(pathlib.Path(directoryname)).mkdir(parents=True, exist_ok=True)
        os.mkdir(os.path.join(filepath, directoryname))
        return "\nRegistered user successfully."


    def login(self, user_Id, psw):
        '''This function is used to login the user, when respective credentials
        are provided by the user.
        --------
        When the username and password provided by the user matches the previous
        register data, then the user is allowed to login.
        --------
        Displays "Username not registered" when the credentials provided doesnot
        match the previous register data.
        --------
        Displays "Wrong password", if the entered password does not match the registered
        username.'''
        l={}
        liu=[]
        lip=[]
        #logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        loginuser = pandas.read_csv('ServerAccessSession/logged_in_Users.csv')
        self.session()
        l=self.createdusers.to_dict('split')
        n = len(l['data'])
        for i in range(0,n):
            liu.append(l['data'][i][0])
            lip.append(l['data'][i][1])
        if self.is_login:
            return "\nAlready logged in"       
        if user_Id not in liu:
            return "\nUsername not registered"
        if psw not in lip:
            return "\nWrong password!"
        if user_Id in loginuser['username'].tolist():
            return "\nLogged in from different address"

        self.is_login = True
        self.user_Id = user_Id
        self.client_directory = ""
        tmoment = pandas.DataFrame(columns=['username'])
        tmoment['username'] = [user_Id]
        loginuser = loginuser.append(tmoment)
        loginuser.to_csv('ServerAccessSession/logged_in_Users.csv', index=False)

        return "\nLogin completed."


    def quit(self):
        '''This function is used to 'Sign Out' the user from the current login session.'''

        loginuser = pandas.read_csv('ServerAccessSession/logged_in_Users.csv')
        try:
            if self.user_Id in loginuser['username'].tolist():
                login_rest = pandas.DataFrame(columns = ['username'])
                login_rest.to_csv('ServerAccessSession/logged_in_Users.csv', index= False)
            self.user_Id = None
            self.client_directory = ""
            self.is_login = False
            self.rdindex = {}
            return "\nSigned out"
        except KeyError:
            return "\nSigned out"


    def delete(self, user_Id, pws):
        '''This function is used to delete a user's account.
        -------
        NOTE: This service is *only* available to the users with a privilege
        level of ADMIN.
        -------
        If the request is done by a user that does not have admin privileges,
        then the request is denied.
        '''
        n=1
        logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        print((logindata.loc[logindata['username'] == self.user_Id]['isAdmin'].values))
        if self.is_login != True:
            return "\nlogin to continue"
        if int(logindata.loc[logindata['username'] == self.user_Id]['isAdmin'].values) != 1:
            return "\n you should be admin."
        if user_Id not in logindata['username'].tolist():
            return "\nNo user with username "+ user_Id + "found"
        if pws != int(logindata.loc[logindata['username'] == user_Id]['password']):
            return "\nEnter correct password"
        dataf = pandas.DataFrame(columns=['username', 'password', 'isAdmin'])
        for us, psw, priv in zip(logindata['username'].tolist(), logindata['password'].tolist(), logindata['isAdmin'].tolist()):
            if us != user_Id:
                dataf_1 = pandas.DataFrame(columns=['username', 'password', 'isAdmin'])
                dataf_1['username'] = us
                dataf_1['password'] = psw
                dataf_1['isAdmin'] = priv
                dataf = dataf.append(dataf_1)
        dataf.to_csv("ServerAccessSession/Users.csv", index = False)
        logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        
        if self.user_Id == user_Id:
            self.quit()
        
        if (n == 1):
            filepath = "c:/Users/gvalm/Documents/GitHub/oreo/Root/Admin/"
        else:
            filepath = "c:/Users/gvalm/Documents/GitHub/oreo/Root/NotAdmin/"
        path = os.path.join(filepath,str(user_Id))
        rmtree(path)
        return"\nDeleted  " + user_Id + " successfully"

    def change_folder(self, directory):
        '''This function is used to move the current directory for
        the current user to the specified folde residing in the current folder.
        -------
        When the user is provided a username ans password to login, if the name
        does not point to a folder in the current directory, the request is denied.'''

        logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        self.session()

        if not self.is_login:
            return "\nLogin to continue"
        n = int(logindata.loc[logindata['username'] == self.user_Id]['isAdmin'].values)
        if (n == 1):
            filepath = "c:/Users/gvalm/Documents/GitHub/oreo/Root/Admin/"
        else:
            filepath = "c:/Users/gvalm/Documents/GitHub/oreo/Root/NotAdmin/"
        path = os.path.join(filepath,str(self.user_Id))
        totaldir = [e for e in pathlib.Path(path).iterdir() if e.is_dir()]
        path_change = os.path.join(path,self.client_directory, directory)
        if path_change in totaldir:
            self.client_directory = os.path.join(self.client_directory, directory)
            return "\n changed directory to "+directory+"successful"
        return"\nInput correct directory name"


    def list(self):
        '''This function gives nformation about the name, size, date and
        time of creation of the request.
        -------
        It also prints all files and folders in the current working directory
        for issuing the request.
        -------
        It pnly has access to the current directory and can not print
        the information regarding content in sub- directories.'''
        self.session()
        logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        if not self.is_login:
            return "\nLogin to continue!!"
        p = (logindata.loc[logindata['username'] == self.user_Id]['isAdmin'].values)
        if p == 1:
            path = os.path.join("c:/Users/gvalm/Documents/GitHub/oreo/Root/Admin/",str(self.user_Id), self.client_directory)
        else:
            path = os.path.join("c:/Users/gvalm/Documents/GitHub/oreo/Root/NotAdmin/",str(self.user_Id), self.client_directory)
        totaldir = []
        for file_name in path.iterdir():
            totaldir.append([str(file_name), str(file_name.stat().st_size), str(file_name.stat().st_mtime)])
        details = "\nFile|Size|Modified Date"
        for data in totaldir:
            line = " | ".join([data[0], data[1], data[2]]) + "\n"
            details += "-------\n" + line
        return details


    def read_file(self, path):
        '''This function is used to read data from the current
        working directory for the ser issuing the request.
        -------
        If a file with specified name does not exist in the current
        working directory for the user, the request is denied.
        -------
        It closes the currently opened from the file from reading
        when service without a name variable is requested.
        -------
        SUbsequent calls with the file as name will start from the
        beginning of the file.'''
        self.session()

        logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        if not self.is_login:
            return "\nLogin to Continue"
        p = int(logindata.loc[logindata['username'] == self.user_Id]['isAdmin'].values)
        if p == 1:
            path_d = os.path.join("c:/Users/gvalm/Documents/GitHub/oreo/Root/Admin/",str(self.user_Id), self.client_directory)
        else:
            path_d = os.path.join("c:/Users/gvalm/Documents/GitHub/oreo/Root/NotAdmin/",str(self.user_Id), self.client_directory)

        files = []
        for f in pathlib.Path(path_d).iterdir():
            path1 = os.path.join(path_d, f)
            if pathlib.Path(path1).is_file():
                files.append(f)
        if path not in files:
            return "\ngiven file not found"
        t_path = os.path.join(path_d, path)
        if t_path not in list(self.rdindex.keys()):
            self.rdindex[t_path] = 0
        with open(t_path, "r") as fi:
            cont = fi.read()
        old_inx = str(self.rdindex[t_path]*self.char_count)
        indx = self.rdindex[t_path]
        data = cont[indx*self.char_count:(indx+1)*self.char_count]
        self.rdindex[t_path] += 1
        self.rdindex[t_path] %= len(cont)//self.char_count+1
        return "\n"+"Read file from"+old_inx+" to " + str(int(old_inx)+self.char_count)+"are\n"+data

    def write_file(self, path):
        '''
        This function appends data to the file in the diectotry
        as per the command given
        --------
        The file will be written with the data of the user input
        --------
        If data already exists in the file in the directory,
        the new data will be appended to the existing data
        without any data loss.
        '''
        self.session()
        logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        if not self.is_login:
            return "\nLogin to continue!!"
        p = int(logindata.loc[logindata['username'] == self.user_Id]['isAdmin'].values)
        if p == 1:
            path1 = os.path.join("c:/Users/gvalm/Documents/GitHub/oreo/Root/Admin/",str(self.user_Id), self.client_directory, path)
        else:
            path1 = os.path.join("c:/Users/gvalm/Documents/GitHub/oreo/Root/NotAdmin/",str(self.user_Id), self.client_directory, path)
        t_file = []
        for fil in pathlib.Path(path1).iterdir():
            p = os.path.join(path1,fil)
            p1 =pathlib.Path(p)
            if p1.is_file:
                t_file.append(fil)
        if path in t_file:
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


    def create_folder(self, pathnamefolder):
        '''
        This function creates new directory as per the user command
        --------
        The function checks the existing directories before creating
        new ones to avoid duplication.
        ---------
        The root path will be changed based on the privilge of user
        '''
        self.session()
        logindata = pandas.read_csv('ServerAccessSession/Users.csv')
        if not self.is_login:
            return"\nLogin to Continue"
        p = int(logindata.loc[logindata['username'] == self.user_Id]['isAdmin'].values)
        if p == 1:
            curr_dir = "c:/Users/gvalm/Documents/GitHub/oreo/Root/Admin/"
        else:
            curr_dir = "c:/Users/gvalm/Documents/GitHub/oreo/Root/NotAdmin/"
        path1 = os.path.join(curr_dir,str(self.user_Id),self.client_directory)
        total_avail_dir = []
        for sub in pathlib.Path(path1).iterdir():
            if sub.is_dir(os.path.join(path1, sub)):
                total_avail_dir.append(sub)
        if pathnamefolder in total_avail_dir:
            return "\nThis directory is already created"
        os.mkdir(os.path.join(path1,pathnamefolder))
        return"\nSuccess"
