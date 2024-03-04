# Python does not usually let us write more than one function with the same name
# to emulate overloading, we can act conditional on the quantity of arguments

import using_args_kwargs
from using_fn import addThem
import functools

def fnD(*args):
    if len(args)==0:
        return f'there are no keyword arguments'
    elif len(args)==1:
        return f'the only positional argument is {args[0]}'
    elif len(args)>1:
        '''add all the arguments'''
        r = functools.reduce(addThem, args)
        return r

if __name__ == '__main__':
    # call with no args
    print( fnD() )
    # call with one arg
    print( fnD(8) )
    # call with many args
    print( fnD(4,3,7,5,2,5,7,4,2,56) )

