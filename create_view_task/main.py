from db_utils.connection import connect
from db_utils.table_property import TableProperty
from db_utils.db_utils import DBUtils

def connect_and_copy_and_create_table():
    with connect() as conn:
        db_session = DBUtils(conn)
        db_session.create_table(table_property=TableProperty.table_prop)
        db_session.copy_table_from_csv(*TableProperty.copy_table, delimiter=';')

with connect() as conn:
    cursor = conn.cursor()
    cursor.execute("""CREATE VIEW period_view AS 
                      SELECT a.endpoint_id, mode_start, mode_duration, label, reason, operator_name
                      FROM periods a, reasons b, operators c
                      WHERE a.endpoint_id = 500 AND b.endpoint_id =500 AND c.endpoint_id=500""")
    cursor.commit()

"""Запрос для создания представления по условию задачи"""

# CREATE VIEW period_view AS 
# SELECT a.endpoint_id, mode_start, mode_duration, label, reason, operator_name
# FROM periods a, reasons b, operators c
# WHERE a.endpoint_id = 505 AND b.endpoint_id = 505 AND c.endpoint_id = 505