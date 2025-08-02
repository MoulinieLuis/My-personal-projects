functions = []

for i in range (3):
	def func():
		return i
	functions.append(func)
	
for f in functions:
	print(f())
 

"""
This program creates an array of functions that return the value "i"
however there is a trick, when the functions are created all of the return i when the functions is called
so the last value i takes is 2, hence all the functions return the value "2"
"""



functions = []

for i in range (3):
	def func(a=i):
		return i
	functions.append(func)
	
for f in functions:
	print(f())

"""
In order to correct this mistake, we need to use "default arguments"
They are variables created that stores, in this case, the value of i before the function is called, making sure the value of
i is stored immutably.

So what this does is create a variable, in this case indicated with a, that stores the value of i for ever-ish

So when the array is created, all the functions return the value of i in different parts of the for loop
"""