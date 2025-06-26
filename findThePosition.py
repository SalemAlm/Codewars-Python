# When provided with a letter, return its position in the alphabet.

# Input :: "a"

# Output :: "Position of alphabet: 1"

# Note: Only lowercased English letters are tested


My solution: 

def position(letter):
    alphabet= 'abcdefghijklmnopqrstuvwxyz'
    pos=alphabet.index(letter)+1
    return f'Position of alphabet: {pos}'