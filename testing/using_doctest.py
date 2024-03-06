import doctest

def nthpower(d=2, p=4):
    '''return the nth power of a number
    we can write tests within the documentation string
    >>> nthpower(4,3) 
    64
    '''
    return d**p

def cubeIt(a,b):
    '''return all the cubes from a to b
    >>> cubeIt(0,6)
    [0, 1, 8, 27, 64, 125]
    >>> cubeIt(0,101) # doctest:+ELLIPSIS
    [0, 1, 8, ..., 1000000]
    '''
    answers = []
    for i in range(a,b):
        answers.append(i**3)
    return answers


if __name__ == '__main__':
    # print( nthpower(3,7) )
    # print( cubeIt(0, 6) )
    doctest.testmod(verbose=True)