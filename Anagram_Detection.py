# An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

# Note: anagrams are case insensitive

# Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

# Examples
# "foefet" is an anagram of "toffee"

# "Buckethead" is an anagram of "DeathCubeK"

# My solution: 

# write the function is_anagram
def is_anagram(test, original):
    first = test.lower()
    second = original.lower()
    if sorted(first)==sorted(second):
        return True
    else: 
        return False

Cleaner: 

def is_anagram(test, original):
    return sorted(test.lower()) == sorted(test.lower())