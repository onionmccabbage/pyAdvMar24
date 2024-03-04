# it is rare to actually get user input in Python
choice = input('Please enter a positive number ') # this is blocking. The console will await user entry
print(choice) # the data type of ANY user input is string
# we should validate
# if choice isinstance(int):
n = int(float(choice)) # we can type cast anything
print(n, type(n))