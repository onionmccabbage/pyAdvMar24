# normal collections can be mutated with 'append' abd 'pop'
l = []
l.append(True)
l.pop() # remove the last entry

# a double ended queue (deque) allows BOTH ends to be mutated
from collections import deque

def checkPalindrome(word):
    '''check to see if a word is a palindrome'''
    dq = deque(word)
    while len(dq)>1:
        left = dq.popleft() # also appendleft()
        right = dq.pop()
        print(left, right)
        if left != right:
            return False # not a palindrome
    return True # so far it is a palindrome

if __name__ == '__main__':
    print( checkPalindrome('madam') ) # True
    print( checkPalindrome('tenet') ) # True
    print( checkPalindrome('racecar') ) # True
    print( checkPalindrome('done') ) # False