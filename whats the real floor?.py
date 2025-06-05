# Write a function that given a floor in the american system returns the floor in the european system.1  =>  0 
# 0  =>  0
# 5  =>  4
# 15  =>  13
# -3  =>  -3

#my solution: 
def get_real_floor(n):
    if n<13 and n>0: 
        return n-1
    elif n>13: 
        return n-2
    elif n<0: 
        return n
    else:
        return n
    

#better solution: 
def get_real_floor(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2

#same as my solution but neater