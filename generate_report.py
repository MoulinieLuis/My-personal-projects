#!/usr/bin/env python3

'''
The line above is a script that tells the CMD this very program is gonna be executed with the "python3" tool to only use the script:
./generate_report.py

NOTE: Remember save this file with that name
'''

import csv
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(dict(data))
    
    return employee_list

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
  
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
  
    return department_data

def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()



employee_list = read_employees('/home/student/data/employees.csv')
dictionary = process_data(employee_list)
write_report(dictionary, '/home/student/data/report.txt') #Writes the final report

'''
This program wont work because we don't have a CSV file with the name "employees.csv".
'''