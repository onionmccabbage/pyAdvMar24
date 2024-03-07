from threading import Thread
import time

def fn():
    while True:
        print('in subthread')
        time.sleep(0.2)


if __name__ == '__main__':
    # a = Thread(target = fn, daemon = False) # KEEPS RUNNING
    a = Thread(target = fn) # KEEPS RUNNING
    # a = Thread(target = fn, daemon = True)
    a.start()
    time.sleep(1)
    print('XXXXXX\nmain thread finished\nXXXXXX')