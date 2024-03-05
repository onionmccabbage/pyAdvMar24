# Python has some standard settings e.g. stdin and stdout
# stdin is used whenever we ask for user input (the console)
# stdout is used by print and defaults to the console

import sys

class RedirectOutput():
    '''redirect output to a different stream
    Then recover the original stream'''
    def __init__(self, new_stdout): # called ONCE on first creation
        self.stdout = new_stdout # we should validate!
    # every class has an intrinsic __enter__ and __exit__ which we can override
    def __enter__(self):
        '''The __enter__ method is invoked whenever the class or an intance of the class is used'''
        self.orig_stdout = sys.stdout # make a note of the current stdout
        sys.stdout = self.stdout # redirect sys.stdout to our new stream
    def __exit__(self, exc_type, exc_value, exc_traceback): # we MUST provide these arguments
        '''The __exit__ method is invoked whenever the class or an intance of the class is completed'''
        sys.stdout = self.orig_stdout # redirect sys.stdout to back to what it was

if __name__ == '__main__':
    '''use our redirection with a file access object'''
    # fout = open('my_log.txt', 'a')
    try:
        # this is a very common practice and is very robust
        with open('my_log.txt', 'a') as fout:
            r = RedirectOutput(fout) # our file access bject is not a stream in our class
            try:
                with r: # this calls __enter__ then __exit__
                    print('this will be written to our text file')
                    # no need to close 'r' since 'with will auto close any assets
            except Exception as err:
                print(err)
        # fout.close() # not needed - when hte 'with' ends, it will close fout
    except Exception as err:
        print(err) # if there is an exception, the 'with' will take care of tidying up
    print('and now we are back writing to the console')