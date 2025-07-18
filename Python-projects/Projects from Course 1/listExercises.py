fruits = ["Apple", "Banana", "Grapes", "Kiwi", "Oranges"]

fruits.append("Cherry")

print(fruits)

fruits.insert(5, "Pear")

print(fruits)

fruits.remove("Banana")


#The pop method removes the last element but it keeps the value in cache, s it's highly recommendable to assign the value o a variable
#Like this

newFruit = fruits.pop(0)
print(newFruit)

print(fruits)
print()

#Print the first letter of the first element
print(fruits[0][0])

#Literal change
fruits[3] = "Mango"
""" 
This print function above is gonna print only the G from the first element of the list, which is "Grapes".
This is because we remove Banana and besides we "pop" Apple
"""

