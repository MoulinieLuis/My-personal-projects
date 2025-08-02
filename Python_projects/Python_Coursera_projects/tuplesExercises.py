#Create a program that takes two values fom a user and their email and return a single string


information = [("Luis", "Luis@mail"), ("Moulinie", "Moulinie@mail"), ("John", "John@mail")]

def full_emails(information):    
    result = []
    for name, email in information:
        result.append("Username: {} Email: {}".format(name, email))
    print(result)  

full_emails(information)


#Another example of tuples
def skip_elements(elements):
    result = [] #creates the list to allocate only the even numbers
    for index, element in enumerate(elements): #enumerates returns 2 values, index and value
        if index % 2 == 0: #Check if the index is even
            result.append(element) #Adds the element to the list result if the index is even
    return result #returns the list that only contains even numbers

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))

#This function prints every other value in a list