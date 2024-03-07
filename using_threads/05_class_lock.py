import threading
import sys
import time
import random
import timeit

ticketsAvailable = 1000000

class TicketSeller(threading.Thread):
    '''This class will sell tickets'''
    ticketsSold = 0
    def __init__(self, lock): # each ticket seller will have access to the SAME lock
        threading.Thread.__init__(self)
        self.__lock = lock
        # print('ticket seller starts selling tickets')
    def run(self):
        global ticketsAvailable # this could be a file, a db an API ....
        running = True
        while running:
            self.randomdelay() # hang about ....
            self.__lock.acquire()
            if ticketsAvailable <=0:
                running = False
            else:
                ticketsAvailable -= 1
                self.ticketsSold += 1
                # print(f'Sold a ticket: {ticketsAvailable} remaining')
            self.__lock.release()
        print(f'Sold {self.ticketsSold}')
    def randomdelay(self):
        time.sleep(random.randint(0,4)/256) # 0, 0.25, 0.5 or 0.75 sec

if __name__ == '__main__':
    lock = threading.Lock()
    sellers_l = []
    start = timeit.default_timer()
    # how many threads?
    # threads will be context-switched to run on a core=thread - so more threads will s-l-o-w down
    for _ in range(0, 2048): # the OS will recycle threads - some will need to wait (procedurally)
        seller = TicketSeller(lock)
        sellers_l.append(seller)
        seller.start()
    for s in sellers_l:
        s.join()
    end = timeit.default_timer()
    print(f'total time: {end-start}')
