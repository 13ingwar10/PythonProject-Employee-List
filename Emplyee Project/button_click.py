from create_employee_list import create_list
import os.path
import export_data
import import_data

def button_click():
    command = input('Select command: \n1 - Add a new employee \n2 - Search for information \n3 - Exit \n')
    if command.lower() == '1':
        create_list()
        export_data.write()
        print('-' * 20)
        button_click()
    elif command.lower() == '2':
        create_list()
        import_data.read()
        print('-' * 20)
        button_click()
    elif command.lower() == '3': quit
    else:
        print('Error! No command is found')
    return True