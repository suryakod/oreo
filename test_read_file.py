# f = open('test.txt', 'r')
# file_data = f.read()
# print(file_data)
# f.close()

# with open("C:\Users\Raashita Samrudhi\Desktop\TCPIP\root\test.txt") as f:
#     file_data = f.read()
#     print (file_data)

from os import path
PATH = "C:\Users\Raashita Samrudhi\Desktop\hello.txt"
if path.exists(PATH) and path.isfile(PATH):
    print "File does exist"
    f = open("hello.txt",'r')
    if f.mode =='r':
        data = f.read(100)
    print(data)
else:
      print "File doesn't exist!" 

