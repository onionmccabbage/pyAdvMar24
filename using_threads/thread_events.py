from threading import Thread, Event
import time

event = Event() # we can use eents to communicate from threads

class SomeClass:
    def __call__(self, n):
        global event
        print(f'Waiting for an event...')
        event.wait()
        print(f'{n} continuing after the event')

if __name__ == '__main__':
    m1 = SomeClass()
    m2 = SomeClass()
    t1 = Thread(target=m1, args=('A',))
    t2 = Thread(target=m2, args=('B',))
    t1.start()
    t2.start()
    # wait on the main thread
    time.sleep(4)
    event.set() # trigger the event to happen
    t1.join()
    t2.join()
