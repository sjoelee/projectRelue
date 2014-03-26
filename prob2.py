"""
Find the sum of even-valued terms in the Fibonacci sequence (up to 4 million).

Solution: We observe that the Fibonacci sequence has a pattern that follows:

odd, odd, even, odd, odd, even...

Hence we create an array of size three which we iteratively update. Each 
element within the array will be determined by the sum of the other two
elements. Since we know that the even values are always going to be in the
third element of the array (at index 2), we won't have to keep track of where
the even numbers are. 

Alternative solutions can include checking if the value is even at every
iteration, which could be equally complex (considering I check if the idx
is divisible by 3 everytime. 
"""

def sumFibEven(limit):
    arrayFib = [1, 1, 2]
    # idx = 0
    total = 0

    # APPROACH #1
    #
    # while arrayFib[idx % 3] <= limit:
    #     if (idx % 3 == 0):
    #         total += arrayFib[2] # sum the even values 
    #     arrayFib[idx % 3] = arrayFib[(idx + 1) % 3] + arrayFib[(idx + 2) % 3]
    #     idx += 1

    # APPROACH #2
    #
    # A bit unreadable, but there is no idx variable to calculate,
    # no need to increment idx and take the modulo, and no conditional statement
    while arrayFib[2] <= limit:
        total += arrayFib[2]
        arrayFib[0] = arrayFib[1] + arrayFib[2]
        arrayFib[1] = arrayFib[0] + arrayFib[2]
        arrayFib[2] = arrayFib[0] + arrayFib[1]
    return total

if __name__=="__main__":
    total = sumFibEven(4000000)
    print total
