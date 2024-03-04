class NumberFun():
    def __init__(self, num):
        self.num = num # use the setter method
    def __str__(self):
        return f'''The {self.findEvenOdd()} number {self.num} squared is {self.findSquare()}
and the square root of {self.num} is {self.findSqrt()}
It is {self.findIfSquareNum()}''' # use the accessors
    def findSquare(self):
        return self.__num ** 2
    def findSqrt(self):
        return self.__num ** 0.5
    def findEvenOdd(self):
        return 'even' if self.num%2 == 0 else 'odd'
    def findIfSquareNum(self):
        r = self.findSqrt()
        if r==int(r):
            return 'a square number'
        else:
            return 'not a square number'
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num):
        if type(num) == int and num > 0:
            self.__num = num
        else:
            self.__num = 1 # sensible default

if __name__ == '__main__':
    n = int(float(input('Enter a number: ')))
    r = NumberFun(n)
    print(r)
    # can we access name-mangled properties?
    # print( r.__num ) # fails
    r.__num = 99 # seems to work, but in fact makes an arbirary new property of 'r'
    # remember - everything is an object and all objects always allow arbitrary properties
    print(r.num) # does not actually affect the value of __num