"""
This program is used to traing recursion with Python
"""

def factorial(number): #function definition
    print("Factorial called with ", number)
    if number < 2: #Base case
        print("Returning 1")
        return 1 #The value returned by the base case
    
    result = number * factorial(number-1) #The function calls itself substracting 1
    print("Returning", result, "for factorial of ", number)
    return result
	
factorial(4)