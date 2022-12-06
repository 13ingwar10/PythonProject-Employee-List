import csv
import os.path

list_header = ['Pers. id','Name', 'Surname', 'Tel. number', 'Position','Notice']

def create_list():
    if not os.path.exists('employee_list.csv'):
        with open('employee_list.csv', 'w', encoding='utf-8') as el:
            writer = csv.writer(el, delimiter=';')
            writer.writerow(list_header)
