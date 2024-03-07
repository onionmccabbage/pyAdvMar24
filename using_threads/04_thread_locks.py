import threading

# All threads for a particular Python execitable share the same resources
# there is ONE copy of Python, ONE set of data (memory etc)
# Each thread has its own heap of memory
# we can lock shared resources to maske the thread safe

counter=1
# if we provide a lock, it becomes a global asset
lock = threading.Lock() # we can use a lock to make resources thread safe

def workerA():
    '''this wprker will access the global counter to increment it'''
    global counter
    lock.acquire() # we have exclusive access to the lock
    try:
        while counter <10:
            counter += 1
            print(f'worker A increments to {counter}')
    except Exception as err:
        print(err)
    finally:
        lock.release()

def workerB():
    '''this wprker will access the global counter to decrement it'''
    global counter
    lock.acquire()
    try:
        while counter >-10:
            counter -= 1
            print(f'worker B decrements to {counter}')
    except Exception as err:
        print(err)
    finally:
        lock.release()

if __name__ == '__main__':
    # workerB()
    # workerA()
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    t2.start() # with the lock, whichever thread starts first will win
    t1.start() 
    t1.join()
    t2.join()