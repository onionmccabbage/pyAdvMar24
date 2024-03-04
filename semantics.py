# why would we use a class?

# there are many types in Python (Python is not strictly typed)
flag = True # or False, a boolean
age = 37 # an integer
intelligence = 198.345 # float
greet = 'hello' # string (an immutable collection of characters)
# other collections
my_tup = (5,4,7,3,8,'any type', False) # a tuple: immutable indexed collection of any types
my_list = [4,3,8,5,23,8,False,age] # a list: mutable indexed collection of any types
my_set  = {4,7,9,3,5,1,9} # a set: collection of unique members
my_dict = {"id":"Floela", "hero":True} # dictionary is not indexed by number

print(greet[0:4]) # 'hell' [start:stop-before:step]
print(my_tup[3:6]) #  [start:stop-before:step]
print(my_set)
print(my_dict['id'])

# perhaps we need data about a shape
t = (3, 4.56, 'red')
l = [4, 5.23, 'green']
# none of the built in collections can validate members
d = {'shape':'hexagon', 'sides':-6, 'size':'really big', 'colour':True}