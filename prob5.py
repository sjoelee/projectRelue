"""
Problem: Find the smallest positive number that is evenly divisible by all
the numbers from 1 to 20.

Solution: Determine the primes from 1 to 20. These are the numbers that do not
have common factors amongst all the other ones. The solution must be divisible
by all these primes. The other non-prime numbers are products of these primes
raised to some power. So we need to figure out how many multiples of a prime
we are missing and multiply that with the product of primes that already exist.
"""
import math as math

"""
Determine all the prime values from start to end
"""
def findPrimes(start, end):
    l_primes = []
    for val in range(start, end+1):
        if isPrime(val):
            l_primes.append(val)
    return l_primes

def isPrime(value):
    int_range_bd = int(math.floor(math.sqrt(value)))
    for val in range(2, int_range_bd + 1):
        if value % val == 0:
            return False
    return True
    
def findSmallestMultiple(start, end):
    if start <= 0 or end <= 0:
        exit
    if start == 1:
        start = start+1
    l_primes = findPrimes(start, end)
    print l_primes

if __name__=="__main__":
    s_multiple = findSmallestMultiple(1, 20)
