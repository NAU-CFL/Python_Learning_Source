#Write a Python function named modCount that is given a positive integer,
#n, and a second positive integer,
#m <= n, and returns how many numbers between 1 and n are evenly divisible by m.

def modCount(n,m):
    if n>=0 and m<=n:
        for i in range(n):
            if i%m==0:
                print(i)
    else:
        return False
