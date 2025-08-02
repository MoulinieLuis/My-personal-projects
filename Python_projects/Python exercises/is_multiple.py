'''
Write a Python program that takes two values and determines if the first value is a multiple of the second value.
True if n is multiple of m, that's, n= mi for some integer i., and False otherwise.
'''

def is_multiple(num1, num2):
    if num2 == 0:
        print("You cannot divide by zero")
        return False
    if num1 % num2 != 0:
        print(f"{num1} is not a multiple of {num2}")
        return False
    print(f"{num1} is a multiple of {num2}")
    return True

num1, num2 = map(int, input("Enter the numbers separated by a space: ").split())

is_multiple(num1, num2)
