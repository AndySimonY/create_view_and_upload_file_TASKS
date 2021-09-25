from utils import get_file_path

class DBUtils:

    def __init__(self, connection):
        self.conn = connection

    def create_table(self, table_property=None):
        cursor = self.conn.cursor()
        if isinstance(table_property, list or tuple):
            for table in table_property:
                sub_query = ''
                try:
                    table_name = table['table_name'].upper()  
                except KeyError:
                    raise f'В свойствах таблицы отсутствует поле table_name, пожалуйста добавьте его в свойства'
                for col_name,col_type in table.items():
                    if col_name == 'table_name':
                        continue
                    col_name, col_type = str(col_name).upper(), str(col_type).upper()
                    sub_query += f'{col_name} {col_type}, '
                sub_query = sub_query[:-2]
                cursor.execute(f"""CREATE TABLE {table_name} ({sub_query})""")
        else:
            try:
                table_name = table_property['table_name'].upper()  
            except KeyError:
                raise f'В свойствах таблицы отсутствует поле table_name, пожалуйста добавьте его в свойства'
            sub_query = ''
            for col_name,col_type in table_property.items():
                    if col_name == 'table_name':
                        continue
                    col_name, col_type = str(col_name).upper(), str(col_type).upper()
                    sub_query += f'{col_name} {col_type}, '
            sub_query = sub_query[:-2]
            cursor.execute(f"""CREATE TABLE {table_name} ({sub_query})""")

    def copy_table_from_csv(self, *args, delimiter=','):
        cursor = self.conn.cursor()
        for copy_data in args:
            csv_filepath = get_file_path(copy_data[1])
            print(csv_filepath)
            if not isinstance(copy_data[0], str):
                raise "Ошибка проверьте правильность вводивых данныйх\n\
                        на месте имени таблицы находятся не строковые данные"
            with open(csv_filepath, 'r', encoding="utf-8") as f:
                    columns = f.readline().replace(f'{delimiter}', ',').replace('\n', '')
                
            query = f"""COPY {copy_data[0]}({columns}) FROM '{csv_filepath}' DELIMITER '{delimiter}' CSV HEADER"""
            cursor.execute(query) 
        print('The tables were copied successfully!')