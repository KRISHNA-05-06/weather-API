import mysql.connector

def connection():
    con = mysql.connector.connect(
        user = 'root',
        host = 'localhost',
        database = 'weather',
        passwd = 'Ksks@0506'
    )

    return con