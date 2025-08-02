#Invert a number

'''
This program takes a number from the user and inverts it
'''

def invert_number(n):
    result = 0
    flag = 0
    
    if n < 0:
        n = n * (-1)
        flag = 1
    
    while n > 0:
        pivot = n % 10
        result = (result * 10) + pivot
        n = n // 10
    
    if flag == 1:
        result = result * (-1)
        return result
    
    return result

n = int(input("Please insert a number: "))

print("The inverted number is:", invert_number(n))