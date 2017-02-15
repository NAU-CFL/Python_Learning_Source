#Write a Python function named ordered3 that is passed three integers, and
#returns true if the three integers are in order from smallest to
#largest, otherwise it returns false.

def ordered3(a,b,c):
    if a<b and b<c:
        return True
    else:
        return False
