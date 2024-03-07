import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(1024) # this will be a byte string
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f'Received {message!r} from {addr!r}')
    print(f'Send message: {message!r}')
    writer.write(data)
    await writer.drain() # wait for the buffer to empty
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_echo, '127.0.0.1', 8888)
    
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    # its recommended to use asyncio.run()
    asyncio.run(main())
