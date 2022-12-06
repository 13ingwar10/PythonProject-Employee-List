import csv
import pandas
from create_employee_list import list_header

def read():
    mode = int(input('Select search type: \n1 - By pers. id \n2 - By name \n3 - By surname \n'))

    request = list(input('Select data for show: \n1 - Pers. id \n2 - Name \n3 - Surname \n4 - Tel. number \n5 - Position \n6 - Notice \n'))
    request = list(map(int, request))

    print(request)

    for i in range(len(request)):
        if list_header[request[i]-1] not in request:
            request[i] = list_header[request[i]-1]

    token = []
    token = list(map(str,input(f'Enter {list_header[mode-1]} to start (or leave empty to see all employees) \n').split()))

    df = pandas.read_csv('employee_list.csv', sep=';', header=None)
    df = df[1:]
    df.columns = list_header

    if len(token) == 0:
        print(df[request])
    else:
        df_new = df.loc[df[list_header[mode-1]] == token[0]]
        if df_new.shape[0] > 0:
            print(df_new[request])
        else:
            print(f"Nobody with {list_header[mode-1]} {token[0]} is found")
