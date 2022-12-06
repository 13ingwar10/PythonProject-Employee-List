import csv
import random
import pandas
from create_employee_list import list_header

def write():
    new_employee = [random.randint(100000, 999999)]

    with open('employee_list.csv', 'r') as f:
        data = pandas.read_csv('employee_list.csv', sep=';', header=None)
        data = data[1:]
        data.columns = list_header
        while(new_employee[0] in data[list_header[0]]):
            new_employee[0] = [random.randint(100000, 999999)]

    for element in list_header[1:]:
        new_employee.append(input(f'Enter Data: {element} \n'))

    with open('employee_list.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')
        writer.writerow(new_employee)
        print(f"Data is successfully added! Personal id {new_employee[0]} is assigned")
