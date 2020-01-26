'''
This file is the server program using async I/O
--------
'''
import asyncio
import signal
from Userclass import User

signal.signal(signal.SIGINT, signal.SIG_DFL)

def clientRequest(usr, message):
    '''
    This function initiates the functions for given commands for user
    '''
    usr.session()
    #if str(usr.user_Id) not in usr.createdusers['username'].tolist():
    #return usr.quit()

    message = message.rstrip("\n").rstrip(" ").lstrip(" ")
    if message.split(" ")[0] == "commands":
        return usr.commands()
    if message.split(" ")[0] == "register":
        if len(message.split(" ")) == 4:
            return usr.register(message.split(" ")[1], message.split(" ")[2], message.split(" ")[3])
        return "Enter correct command"
    if message.split(" ")[0] == "logout":
        return usr.quit()
    if message.split(" ")[0] == "quit":
        return usr.quit()
    if message.split(" ")[0] == "login":
        if len(message.split(" ")) == 3:
            return usr.login(message.split(" ")[1], message.split(" ")[2])
        return "Enter correct command"
    if message.split(" ")[0] == "list":
        return usr.list()
    if message.split(" ")[0] == "change_folder":
        if len(message.split(" ")) == 2:
            return usr.change_folder(message.split(" ")[1])
        return "Enter correct command"
    if message.split(" ")[0] == "read_file":
        if len(message.split(" ")) == 1:
            return usr.read_file(message.split(" ")[1])
        return "Enter correct command"
    if message.split(" ")[0] == "write_file":
        if len(message.split(" ")) == 2:
            return usr.write_file(message.split(" ")[1])
        return "Enter correct command"
    if message.split(" ")[0] == "create_folder":
        if len(message.split(" ")) == 2:
            return usr.create_folder(message.split(" ")[1])
        return "Enter correct command"
    if message.split(" ")[0] == "delete":
        if len(message.split(" ")) == 2:
            return usr.delete(message.split(" ")[1])
        return "Enter correct command"
    return "Enter the correct command "



async def handle_echo(reader, writer):
    '''
    This funtion acknowledges the connection from the client,
    acknowledges the messages from the client
    '''
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"
    print(message)
    #print(os.getcwd())
    usr = User()
    #print(usr._addr)
    #print(type(usr))
    while True:
        data = await reader.read(4096)
        message = data.decode().strip()
        if message == 'exit':
            break

        print(f"Received {message} from {addr}")
        #print(f"Send: {message}")
        mymsg = clientRequest(usr, message)
        msg = str(mymsg).encode()
        writer.write(msg)
        await writer.drain()
    print("Close the connection")
    writer.close()


async def main():
    '''
    This function starts the connection between the server and client
    '''
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8080)


    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


asyncio.run(main())
