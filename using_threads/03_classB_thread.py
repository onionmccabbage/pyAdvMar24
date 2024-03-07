from threading import Thread
import time
import timeit
import random

class MyClassB: # implicitly inherit from object
    '''This class does not inherit from Thread'''
    '''to call this as a thread we must write a __call__ method'''
    def __call__(self, n): # __call__ lets us target this function as a thread
        msg = ''
        for i in range(0,10):
            msg += f'thread {n} is sleeping' + '\n' # remember print is i/o bound (slow)
            time.sleep(random.random()*0.1)
        print(msg) # try to minimize the i/o operations

if __name__ == '__main__':
    cA = MyClassB()
    # we might need a large quantity of threads
    threads_l = []
    for _ in range(0,1024):
        threads_l.append(Thread(target=cA, args=(_,)))
    print('Main thread has spawned several child threads')
    # we start all the threads
    # start = time.time() # time only looks at the clock
    start = timeit.default_timer() # timeit tries to spot only those things that Python does
    for item in threads_l:
        item.start() # we cannot avoid starting the threads proceduraly
    for item in threads_l:
        item.join()
    # end = time.time()
    end = timeit.default_timer()
    print(f'total time ({end-start})')