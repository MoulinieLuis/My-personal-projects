"""
This program aims to understand how to work with strings
"""

#Slicing strings

#joining strings


#A more complex script
def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

format_phone('2025551212')

#The output is (202) 555-1212