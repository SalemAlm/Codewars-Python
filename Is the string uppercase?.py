#Is the string uppercase?
#ask
#Create a method to see whether the string is ALL CAPS.

#Examples (input -> output)
#"c" -> False
#"C" -> True
#"hello I AM DONALD" -> False
#"HELLO I AM DONALD" -> True
#"ACSKLDFJSgSKLDFJSKLDFJ" -> False
#"ACSKLDFJSGSKLDFJSKLDFJ" -> True
#In this Kata, a string is said to be in ALL CAPS whenever it does not contain any lowercase letter so any string 
#containing no letters at all is trivially considered to be in ALL CAPS.

# def is_uppercase(inp)
#     return not any(c.islower() for c in inp)
 
#using "not" reverses the return bolean, so if it is gonna say true then putting not makes it say false
#any then covers any values in the inp
#islower() checks if all the inputs are lowercase 
#c is a compacted for loop


