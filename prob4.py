"""
Problem: Find the largest palindrome made from the product of two 3-digit 
numbers

Notes: What is a palindrome? For a word, the letters must mirror across the
middle. 

If I go through all possible products, I have 9*10*10*2 possibilities = 1800.

1. How do you determine that the first and last values are the same?
2. How do you determine the middle values themselves are a palindrome?

Seems like there's some recrusion here. 

03-31-2014: I brute forced this knowing that I should start from 999 and work 
my way down. I knew the largest palindrome would exist somewhere between 999
and 900, I decided at the very worst case, I would go through 10,000 iterations.
I'll need to find a better more efficient way of this rather than just doing
grid search.
"""

def findLargePalindrome():
    isPalindrome = True
    for val1 in range(999, 900, -1):
        for val2 in range(999, 900, -1):
            prod = val1 * val2
            prod_str = str(prod)
            len_range = prod_str.__len__()/2
            prod_str_len = prod_str.__len__()
            for idx in range(0, len_range):
                if (prod_str[idx] == prod_str[prod_str_len - idx - 1]):
                    continue
                else: 
                    isPalindrome = False
            if isPalindrome:
                return (val1, val2, prod)
            isPalindrome = True

                
if __name__=="__main__":
    (val1, val2, prod) = findLargePalindrome()
    print "Largest palindrome is: %d * %d = %d " % (val1, val2, prod)
