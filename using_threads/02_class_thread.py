from threading import Thread
import time
import random
from typing import Mapping

class MyClass(Thread):
    '''Any class may be invoked as a thread, but it is easiest to inherit from Thread'''
    def __init__(self, n, t):
        # we use 'Thread' rather than 'super' since Thread will implicitly pass required args
        Thread.__init__(self): # call the initializer of the parent class
        # super().__init__(group, target, name, args, kwargs, daemon=daemon) # super would mean writing all teh args ourself
        self.n = n # we could validate with @property get/set
        self.t = t
    # every thread has a 'run' method which we can override
    def run(self):
        '''When this thread is invoked it will run this method (on a new thread)'''
        for i in range(0,10):
            print(f'{self.n} is sleeping')
            time.sleep(random.random()*0.1)

if __name__ == '__main__':
    print('The main thread will invoke some child threads')
    tA = MyClass('A', True)
    tB = MyClass('B', 'wow')
    tC = MyClass('C', [])
    tD = MyClass('D', (5,4,3,2))
    tA.start()
    tB.start()
    tC.start()
    tD.start()
    print('The main thread carries on')