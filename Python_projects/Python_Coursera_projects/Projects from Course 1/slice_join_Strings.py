"""
This program aims to understand how to work with strings
"""

#Slicing strings
string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”


#joining strings
greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"

#A more complex script
def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

format_phone('2025551212')

#The output is (202) 555-1212