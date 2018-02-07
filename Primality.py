from math import *
from random import randint
from datetime import datetime

primelist=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
           71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
           151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
           233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
           317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409,
           419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
           503, 509, 521, 523, 541]

primeproduct=1
for i in primelist:
    primeproduct*=i


def binary(x):
    """ returns the binary form of an integer x
    returns an int
    """
    if x==0:
        return '0'
    L=[]
    y=int(ceil(log(x+1)/log(2)))
    L.append('1')
    x=x-2**(y-1)
    for i in range(y-1):
        if x-2**(y-i-2)<0:
            L.append('0')
        else:
            L.append('1')
            x=x-2**(y-i-2)
    z=''
    for i in L:
        z=z+i
    return z

def GetTime():
    t=datetime.now()
    t=str(t)
    second=float(t[17:24])
    minute=float(t[14:16])
    hour=float(t[11:13])
    return second+minute*60+hour*60**2

def binlist(x):
    """Takes in a number and returns a list of exponents in binary"""
    L=[]
    while x>0:
        a=int(log(x)/log(2))
        L.append(a)
        x-=2**a
    return L

def exponent(x,y):
    """Calculates x**y"""
    global b
    b=binlist(y)
    b.sort()
    a=1
    for i in b:
        c=x
        for j in range(i):
            c=c**2
        a=(a*c)%(y+1)
    return a

def recurse(x,y,c):
    global m
    if y%2==0:
        even= True
    else:
        even=False
    if y==1:
        return x
    if even:
        j=recurse(x,y/2,c)%c
        return (j**2)
    else:
        k=recurse(x,(y-1)/2,c)%c
        return (x*k**2)
    
def loopExp(x,n):
    y=1
    c=n
    n=n-1
    while n>1:
        if n%2==0:
            x=(x*x)%c
            n=n/2
        else:
            y=(x*y)%c
            x=(x*x)%c
            n=(n-1)/2
    return (x*y)%c

def Exp(x,y):
    c=y
    w=recurse(x,y-1,c)
    return w%c


def prime(n):
    if n in primelist:
        return True
    if n==2:
        return True
    global primeproduct

    if loopExp(primeproduct,n)!=1:
        return False
    for i in range(1):
        a=1
        for i in range(100):
            a*=randint(2,n-1)
        if loopExp(a,n)!=1:
            return False
        else:
            return True

n = int(input("Enter a number:"))
p = prime(n)
if p:
    print("That number is prime")
else:
    print("That number is not prime")
