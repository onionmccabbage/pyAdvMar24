
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
    