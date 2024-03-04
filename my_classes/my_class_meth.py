# we may choose to have methods that belong to the class, 
# rather than to any instance of the class

class Duck():
    count=0 # this variable is now a property of the Duck class
    def __init__(self, name):
        self.__name = name # we could write get/set and validators
        Duck.count += 1
    @classmethod # this method belongs to the Duck class
    def howMany(cls):
        return f'the Duck clas has {cls.count} instances'
    
if __name__ == '__main__':
    d1 = Duck('Howard')
    d2 = Duck('Mallard')
    d3 = Duck('Eider')
    print(Duck.howMany())
    print(Duck.count) # 3