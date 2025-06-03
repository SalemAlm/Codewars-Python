# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

# My solution: 
def get_grade(s1, s2, s3):
    final = (s1 + s2 + s3)/3
    if final>=90:
        return "A"
    elif final>=80:
        return "B"
    elif final>=70:
        return "C"
    elif final>= 60: 
        return "D"
    else:
        return "F"
        

# better solution: Better syntax for readability

def get_grade(s1, s2, s3):
    mean = sum([s1,s2,s3])/3
    if mean>=90: return 'A'
    if mean>=80: return 'B'
    if mean>=70: return 'C'
    if mean>=60: return 'D'
    return 'F'
    