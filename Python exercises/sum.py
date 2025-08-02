'''
This program return the sum of all the square numbers previous to the number given by the user.
'''

def sum_of_squares(n):
    total = 0
    if n < 0:
        print("The number given is 0 try with a positive number")
        return 0
    
    for i in range(n):
        total += i * i
        
    return total

number = int(input("Enter a positive number: "))
result = sum_of_squares(number)

print(f"The sum of all square numbers previous to {number} is: {result}")