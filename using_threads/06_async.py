# see https://docs.python.org/3/library/asyncio.html
import asyncio

# any function can be asyncronous
async def main():
    # we may await an outcome - this is blocking
    await asyncio.sleep(1) # ilustrate a log running process
    print('hello')

if __name__=='__main__':
    # asyncio.run(main())
    # or (recommended)
    with asyncio.Runner() as runner:
        runner.run(main())
        runner.run(main())
    print('are we there yet')