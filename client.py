'''
This file is the client program using async I/O 
--------
The connection is made with the server using local host
--------
After the connection has been established the 
user commands are executed as per the Userclass
--------
The connection is closed based on the user request 
'''


import asyncio


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8080)
    message = ''
    while True:
        message = input('Enter command ::\n')
        if message == "":
            print("Invalid Command\n")
            continue

        writer.write(message.encode())
        data = await reader.read(4096)
        print(f'Received: {data.decode()}')
        if message.lower() == "quit":
            break
    print('Close the connection')
    writer.close()


asyncio.run(tcp_echo_client())