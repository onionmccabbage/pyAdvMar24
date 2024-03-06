from custom_decorator import showArgs

# use a generator
@showArgs
def geny(n=3):
    '''generate a load of values and return them in a tuple'''
    r = tuple(range(0,n)) # this generator populates a tuple
    return r

if __name__ == '__main__':
    t = geny(1000)
    print(t, type(t))
