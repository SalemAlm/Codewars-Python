# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"

# Solution: 

def bmi(weight, height):
    if weight/(height*height)<=18.5:
        return "Underweight"
    elif weight/(height*height)<=25:
        return "Normal"
    elif weight/(height*height)<=30:
        return "Overweight"
    elif weight/(height*height)>30:
        return "Obese"
    
