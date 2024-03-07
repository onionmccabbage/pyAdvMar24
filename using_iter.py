# we can make anything iterable - such as our own class

class Evens:
    '''this class lets us iterate through even numbers'''
    def __init__(self, limit):
        self.__limit = limit
        self.__start = 0
    def __iter__(self):
        '''to make a class iterable simply override the __iter__ method'''
        return self # simple as that
    def __next__(self):
        '''Once the class is iterable we can override __next__'''
        if self.__start > self.__limit:
            raise StopIteration
        else:
            rval = self.__start
            self.__start += 2
            return rval
        
if __name__ == '__main__':
    e = Evens(10)
    print(e.__next__()) # 0
    print(e.__next__()) # 2
    print(e.__next__()) # 4
    # we can iterate over the remaining values
    for _ in e:
        print(_)
    # print(e.__next__()) # exception
    