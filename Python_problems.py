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


#Problem 1
def odd_or_even(n):
    
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
        
n = int(input("Enter a number: "))
print(odd_or_even(n))


#Problem 2
def ends_with_7(n):
    pivot = n % 10
    
    if pivot == 7:
        return True
    else:
        return False
    '''
    The whole if above coulb be replaced by the line "return pivot == 7"
    '''
        
n = int(input("Enter a number: "))
print(ends_with_7(n))

#Problem 3
def sum_of_digits(n):
    result = 0
    
    if n < 0:
        n = n * -1
    
    while n > 0:
        pivot = n % 10
        result += pivot
        n = n // 10
    
    return result
    
n = int(input("Enter a number to sum it: "))
print(sum_of_digits(n))

#Problem 4
def count_vowels(string):
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    counter = 0
    
    for letter in string:
        if letter in list_vowels:
            counter += 1
    
    return counter

string = input("Insert a string, I'll tell how many vowels it has: ")
print("Your string has:", count_vowels(string), "vowels")

#Problem 5
def is_palindrome(string):
    string = string.lower()
    string = string.replace(" ", "")
    
    reverse_string = string[::-1]
    
    if string == reverse_string:
        return "Your string is a palindrome"
    return "Your string is not a palindrome"
    
string = input("Enter a word or phrase to see if it's a palindrome: ")
print(is_palindrome(string))

#Problem 6
def remove_duplicates(word):
    
    seen = set()
    new_word = []
    
    for letter in word:
        if letter not in seen:
            seen.add(letter)
            new_word.append(letter)
    return ''.join(new_word)

word = input("Enter a string")

print(remove_duplicates(word))