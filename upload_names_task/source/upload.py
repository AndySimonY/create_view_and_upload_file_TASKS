import psycopg2
import pandas as pd
from numpy import NaN
import os

def get_file_path(relative_path):
    return os.getcwd() + relative_path

def connect():
    try:
        con = psycopg2.connect(
            database="task_3", 
            user="postgres", 
            password="sleaaels", 
            host="127.0.0.1", 
            port="5432"
        )
        print("Database opened successfully")
        return con
    except(Exception, ConnectionError) as error:
        return error

with connect() as conn:
    cursor = conn.cursor()
    top_players = pd.read_excel(get_file_path(r'\названия точек.xlsm'))
    columns = ''
    list_col_val = []
    for col in top_players.columns.values:
        columns += f'{col},'
        colval = []
        for col_val in top_players[col].values:
            if col_val is NaN:
                col_val = 'null'
            else: 
                col_val = f"'{col_val}'"
            colval.append(col_val)
        list_col_val.append(colval)
    list_col_val = tuple(list_col_val)

    columns = columns[:-1]
    col_val = []
    items = []
    for it in range(len(list_col_val)):
        items.append(f'item{it}')
    items = tuple(items)
    for items in zip(*list_col_val):
        col_val.append(list(map(lambda x: str(x).replace("'", ''), items)))

    col_val_str = ''
    for i in col_val:
        for j in range(len(i)):
            try:
                if int(i[j]):
                    i[j] = int(i[j])
            except:
                pass
        t_val = tuple(i)
        str1 = ''
        for m in range(len(t_val)):
            if isinstance(t_val[m], str) and t_val[m] != 'null':
               str1 += f"'{t_val[m]}',"
            else:
                str1 += f'{t_val[m]},'
            if len(t_val) - m == 1:
                str1 = str1[:-1]
                str1 = f'({str1})'
        col_val_str += f'{str1},'
    col_val_str = col_val_str[:-1]
    query = f"""INSERT INTO endpoint_names ({columns}) VALUES {col_val_str}"""
    cursor.execute(query)