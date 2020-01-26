from Userclass import User

usr = User()

print(usr.register('sur','123','admin'))
print(usr.login('sur',123))
print(usr.delete1('sur',123))