# Code for the greatest common divisor

def gcd(a:int,b:int)->int:
    if a == b:
        return a
    elif b > a:
        a,b = b,a

    while True:
         if a % b != 0:
             temp = a % b
             a,b = b,temp
         else:
             return b



