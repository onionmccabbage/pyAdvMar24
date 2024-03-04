# every function (including methods of a class) may take positional arguments and keyword arguments

def fnA( *args ): # *args will collect ANY positional arguments into a tuple called args
    '''return just the positional arguments'''
    return args

def fnB( **kwargs ): # **kwargs will collect ANY keyword arguments into a dict
    '''return just the keyword arguments'''
    return kwargs

def fnC( *args, **kwargs ):
    return f'The positional arguments are: {args}\nThe keyword arguments are: {kwargs}'

if __name__ == '__main__':
    r = fnA(True, 4,2,78,'wow', [4,3,2])
    print( r, type(r) ) # we expect to see a tuple containing these members
    s = fnB(x=3, y=4, z=5)
    print( s, type(s) ) # we expect to see a dictionary of these members
    # both
    print( fnC() )
    print( fnC(1,2,3,4) ) # only positional
    print( fnC(x=7,y=6) ) # only keyword
    print( fnC(True, 'wow', n=5, q='all done') ) # both

