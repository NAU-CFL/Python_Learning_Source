#Write a Python function named zeroCheck that is given three integers,
#and returns true if any of the integers is 0, otherwise it returns false.

def zeroCheck(a, b, c):
    if 0 in (a,b,c):
        return True
    else:
        return False
