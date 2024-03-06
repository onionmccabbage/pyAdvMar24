# comprehension, generators and yield
# generators
def doComp():
    # a generator does NOT persist its values in memory. Instead it yields them on demand
    stru = (i for i in range(0, 100, 2)) # here we deal comprehensively with each member of the range
    # print(type(stru))
    return stru # return our generator

# comprehension - means dealing comprehensively wit hevery member of a structure
# e.g. a list, a tuple a dict or a generator
def demoComprehension():
    # we need some structures
    t = (5,4,3,2,1) # tuple
    l = [9,8,7,6,5] # list
    s = doComp()    # generator
    # tuple comprehension
    print((i for i in t)) # here we make a generator from the comprehension
    print([i for i in t]) # here we persist the comprehension into a list (all values exist in memory)
    # for i in t:
    #     print(i, end=', ')
    print()
    # list comprehension
    print([i for i in l])
    # for i in l:
    #     print(i, end=', ')
    print()
    # generator comprehension
    print([i for i in s])
    # for i in s:
    #     print(i, end=', ')
    print()

   

if __name__ == '__main__':
    '''exercise the local code'''
    s = doComp()
    print(s, type(s))
    print(s.__next__()) # 0 
    print(s.__next__()) # 2
    demoComprehension()
