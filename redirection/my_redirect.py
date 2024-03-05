# Python has some standard settings e.g. stdin and stdout
# stdin is used whenever we ask for user input (the console)
# stdout is used by print and defaults to the console

import sys

class RedirectOutput():
    '''redirect output to a different stream
    Then recover the original stream'''
    def __init__(self, new_stdout):
        pass

if __name__ == '__main__':
    pass