#Creation of a CSV file

import csv

# Data to write
header = ["Name", "Age", "City"] #Defines the header

'''
Note: You can also define the header in the rows list and use a special method to read as a dictionary called dictreader that automatically will recognize the first column is the header.
'''

rows = [
    ["Luis", 23, "Mexico City"],
    ["Ana", 25, "Guadalajara"],
    ["Carlos", 30, "Monterrey"]
]

# Create and write to the CSV
with open("people.csv", "w", newline="") as file: #Remember that "w" means write/overwrite/create_if_not_exists
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    writer.writerows(rows)   # Write multiple rows
