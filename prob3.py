import math as math
"""
To determine the largest prime of a number, we need to divide
the number by the lowest prime (and its power), then its next lowest, and so on.
"""

"""
From the currentPrime, determine the next prime number that divides num. In
order to do so, only consider odd values (because all even numbers except the
number 2 are not primes). Go through each value and see if it's a prime value.
If so, see if it's a divisor of the number
"""
def findNextPrime(currVal):
    while (True):
        currVal += 1
        if (currVal & 1 == 0):
            continue; # skip even values
        if (isPrime(currVal)):
            break
    return currVal

"""
Follows the trial division approach. And since we know a value y = m*n, m and n 
cannot be greater than the sqrt(y), so we have an upperbound to our calculation.

Perhaps a better way of approaching this to not find the squareroot but to use
logs?
"""
def isPrime(val):
    n = 3
    if (val % 2 == 0):
        return False
    else:
        upper_bd = math.floor(math.sqrt(val));
        while (n < upper_bd):
            if (val % n == 0):
                return False
            n += 1
        return True

def determineLargestPrime(num):
    currVal = 2
    currPrime = 2
    if num == 0:
        return 0
    if num == 1:
        return 1
    while (currVal <= num):
        while (num % currVal == 0):
            currPrime = currVal
            num = num / currVal
            if (num == 1):
                return currPrime
        currVal = findNextPrime(currVal)
            
if __name__=="__main__":
    largestPrime = determineLargestPrime(600851475143)
    print "Largest Prime: ", largestPrime
