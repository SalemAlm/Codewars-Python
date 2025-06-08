# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

# For example:

# a = 1
# b = 4
# --> [1, 2, 3, 4]

MY SOLUTION: 

def between(a,b):
    return list(range(a,b+1))
    pass

# Explanation: 

# The range function prints the numbers between a and between

# but it excludes B, so we add a +1 so it includes it

# the List function then turns the number into a list