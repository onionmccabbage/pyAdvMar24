from threading import Thread
import time
import random

# all i/o must be handled by the main thread
# threads are i/o bound - they will be paused for any i/o

def myFn(n):
    '''This is a normal function which can be invoked in teh usual way'''
    time.sleep( random.random()*2 ) # emulate a long-running feature
    print(f'This is function {n}')
    time.sleep( random.random()*2 ) # emulate a long-running feature
    print(f'This is function {n} again')

if __name__ == '__main__':
    # here we run the function proceduraly - one followed by another
    # myFn('A')
    # myFn('B')
    # myFn('C')
    # we can target any function to run it on a thread
    tA = Thread(target=myFn, args=('A',))
    tB = Thread(target=myFn, kwargs={'n':'B'})
    tA.start() #at this point our function will be run on a separate thread
    tB.start()
    print('This comes from the main thread') # the main thread carries on - it is not blocked
    # it is good practice to use join even though it will block the main thread
    tA.join() # this will block the main thread
    tB.join()
    print('All threads have now joined back to the main thread') # main thread blocked until others join