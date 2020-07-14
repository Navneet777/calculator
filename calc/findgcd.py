# find gcd 
import sys
def findGCD(x, y):
   while(y):
       x, y = y, x % y
   return x
