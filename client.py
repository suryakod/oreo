import asyncio


async def tcp_echo_client():
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)
    message = ''
    while True:
        message = input('Enter command ::\n')
        if message == "":
            print("Invalid Command\n")
            continue

        writer.write(message.encode())
        data = await reader.read(100)
        print(f'Received: {data.decode()}',"utf-8")
        if message.lower() == "quit":
            break
    print('Close the connection')
    writer.close()


asyncio.run(tcp_echo_client())