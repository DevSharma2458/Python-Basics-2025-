# First non-repeating char
def first_non_repeat(s):
    for ch in s:
        #Check each character.
        #If it appears only once, return it.
        if s.count(ch) == 1:
            return ch