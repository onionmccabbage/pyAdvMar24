# here we will use named tuples
from collections import namedtuple

def makeTaskTup( tup=tuple() ):
    '''we will define a named tuple to encapulate themembers of a task
    summary, owner, done, id
    We would normally validate these members'''
    task = namedtuple('Task', ['summary', 'owner', 'done', 'id'])
    task.__new__.__defaults__ = (None, None, False, None) # the None type is handy
    # we can unpack the members of the tup by using the asterisk *tup
    t = task(*tup)
    return t

# use pytest
def test_member_access():
    t = makeTaskTup(('finish doing stuff', 'Grace'))
    # we can assert tests
    assert t.summary == 'finish doing stuff'
    assert t.owner   == 'Grace'
    assert (t.done, t.id) == (False, None)

def test_defaults():
    '''make sure the named tuple creates the defaults we expect'''
    t = makeTaskTup()
    s = makeTaskTup((None, None, False, None))
    assert t==s


if __name__ == '__main__': # dunder - double underscore before and after
    # here the test results default  to the standard output (terminal)
    # we could use redirection to persist the test results
    # then we could automate result response
    test_member_access()
    test_defaults()


