'''
Mix and Max
This Python program checks for the max and min number in an array without using the min() and max() build-in functions
'''

def min_and_max(list):
    if not list or len(list) == 0:
        print("The list is empty")
        return None, None
    
    min_value = list[0]  #With this line you can assure to find the right value when for example the list doesn't start in 0
    max_value = 0
    
    for i in list:
        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i
    
    return min_value, max_value

number_list = list(map(int, input("Enter the numbers separated by a space: ").split()))

min_value, max_value = min_and_max(number_list)

print(f"The minimum value is: {min_value} and the maximum value is: {max_value}")