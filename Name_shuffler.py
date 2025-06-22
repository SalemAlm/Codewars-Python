# Write a function that returns a string in which firstname is swapped with last name.

# Example(Input --> Output)

# "john McClane" --> "McClane john"

My solution: 

def name_shuffler(str_):
    name = str_.split()
    return name[1]+' '+name[0]