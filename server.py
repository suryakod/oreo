import asyncio
import signal
import os
from Userclass import User

signal.signal(signal.SIGINT, signal.SIG_DFL)

def clientRequest(usr, message):
    usr.session()
    if str(usr.userId) not in usr.createdusers['username'].tolist():
        return usr.quit()
    message = message.rstrip("\n").rstrip(" ").lstrip(" ")
    if message.split(" ")[0] == "commands":
        return usr.commands()
    if message.split(" ")[0] == "register":
        if len(message.split(" ")) == 4:
            return usr.register(message.split(" ")[1],message.split(" ")[2],message.split(" ")[3])
        return "Enter correct command"
    if message.split(" ")[0] == "logout":
        return usr.quit()
    if message.split(" ")[0] == "quit":
        return usr.quit()
    if message.split(" ")[0] == "login":
        if len(message.split(" ")) == 3:
            return usr.login(message.split(" ")[1],message.split(" ")[2])
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
    addr = writer.get_extra_info('peername')
    message = f"{addr} is connected !!!!"
    print(message)
    #print(os.getcwd())
    usr = User(os.getcwd(),addr)
    #print(usr._addr)
    #print(type(usr))
    while True:
        data = await reader.read(100)
        message = data.decode().strip()
        if message == 'exit':
            break

        print(f"Received {message} from {addr}")
        #print(f"Send: {message}")
        writer.write(clientRequest(usr, message) + '\n'.encode())
        await writer.drain()
    print("Close the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 10000)


    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()



asyncio.run(main())