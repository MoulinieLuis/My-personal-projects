import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open(filename, "r") as file:
    # Read the rows of the file
    rows = csv.reader(file) #Here creates a list of elements to iterate over them
    next(rows) #This ensures the list "rows" start in the second position, because the first one is the header, super important
    # Process each row
    for row in rows:
      name, color, type = row #Unpack the elements of the first list (row) of the list (rows) to work individually in each element
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(color, name, type) #Creates the large string with the values
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))