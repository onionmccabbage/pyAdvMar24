# to access 'reduce' we import functools
import functools


def isOdd(n):
    '''return True if odd False if even'''
    return n%2 !=0 # % means integer division (modulo)

def addThem(m,n):
    '''return the sum of m and n'''
    return m+n

if __name__ == '__main__':
    # this code only runs if this module is being executed directly
    # this code will not run if this module has been impoted elsewhere
    print( isOdd(3) ) # True
    print( isOdd(8) ) # False
    print( addThem(3,4)) # 7
    # we can use our simple functions to apply to many values
    results = map(isOdd, range(0,11) ) # range(start, stop-before, step)
    print(results) # we have a map object - NOT the results of every function call
    # to use a map object, we call the __next__() value
    print( results.__next__() ) # False (0)
    print( results.__next__() ) # True  (1) - it only runs the fn when the __next__ is called
    print( results.__next__() ) # False (2)
    print( results.__next__() ) # True  (3)
    # we can access all the results by putting them into a tuple
    results_t = tuple( results ) # only takes the remaining values from the map object
    print(results_t)

    # we can also use filter
    odds = filter(isOdd, range(-7, 8))
    print(odds) # a filter object. Again, the values will only be calculated on first use
    print(odds.__next__()) # -7
    print(odds.__next__()) # -5
    print(odds.__next__()) # -3
    # we can choose to iterateover a map object or a filter object
    for i in odds: # this will iterate over all remaining filter values
        print(i)

# we also have 'reduce'
