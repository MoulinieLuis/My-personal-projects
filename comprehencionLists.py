"""
This exercise walks you through how to write a list comprehension to create a list of squared numbers (n*n or n**2). It needs to return a list of squares of consecutive numbers between “start” and “end” inclusively. For example, squares(2, 3) should return a list containing [4, 9].
"""

user_range = input("Enter the start and end numbers separated by a space: ").split()
start, end = int(user_range[0]), int(user_range[1])

numbers = print([x**2 for x in range(start, end + 1)])
