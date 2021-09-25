import psycopg2

def connect():
    try:
        con = psycopg2.connect(
            database="<name>", 
            user="postgres", 
            password="<password>", 
            host="127.0.0.1", 
            port="5432"
        )
        print("Database opened successfully")
        return con
    except(Exception, ConnectionError) as error:
        return error
