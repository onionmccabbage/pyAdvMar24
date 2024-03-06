# wecan write a custom decorator

def showArgs(f): # f will be a function object passed in to our decorator
    ''' reveal the positional and keyword arguments of ANY function'''
    def newFunc(*args, **kwargs):
        print(f'Running a function called {f.__name__}')
        print(f'The positional arguments are {args}')
        print(f'The keyword arguments are {kwargs}')
        # we should also run the passed-in function
        return f(*args, **kwargs)
    return newFunc # NB we do not call it

@showArgs # we can use a decorator to augment ANY function (including methods of a class)
def raisePower(m,n):
    '''raise m to the powerr of n'''
    return m**n

@showArgs # a decorator will decorate the function immediately following
# so be careful with multiple decoartors
def squareIt(x):
    '''return the square of x'''
    return x**x

@showArgs
def addThem(x=1, y=2):
    '''return the sum of a+b'''
    return x+y

if __name__ == '__main__':
    '''use our functions'''
    a = addThem(x=4, y=3) # keyword arguments
    s = squareIt(9)       # positional arguments
    r = raisePower(3, n=2)# both
    print(a, s, r)