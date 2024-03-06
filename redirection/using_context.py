#  we can switch context using a contexxt manager
from contextlib import contextmanager
import sys

@contextmanager # this decorator lets us handle context
def outputRedirect( newOutput ):
    '''redirect any printed output to a different context'''
    old_stdout = sys.stdout # remember the current standard ouput stream
    sys.stdout = newOutput
    # NB if a function uses 'yield' then it can keep running even after the end
    yield # our function will yield the next available object to be sent to the output stream
    sys.stdout = old_stdout # return the standard output stream to what it was before

if __name__ == '__main__':
    '''handle context'''
    print('Normal printed output is sent to the console')
    try:
        with open('my_stream.txt', 'a') as fojb:
            with outputRedirect(fojb):
                print('This will be redirected into a persistent text file') # defaults to adding new-line character
                sys.stdout.write('more context-switched output') # no default termination character
    except Exception as err:
        print(err)
    print('All context is returned to the orignal output stream')