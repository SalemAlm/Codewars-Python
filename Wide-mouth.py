# Your goal in this kata is to
#  create complete the mouth_size method this method takes one argument animal which corresponds
#  to the animal encountered by the frog. If this one is an alligator (case-insensitive) return small otherwise return wide.

# solution: 
def mouth_size(animal):
    fixed = animal.lower()
    if fixed == 'alligator':
        return('small')
    else: 
        return('wide')

# the .lower() method forces all characters in the string to lowercase

# Short version: 

def mouth_size(animal): 
    return 'small' if animal.lower() == 'alligator' else 'wide'