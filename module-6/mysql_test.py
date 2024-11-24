import mysql.connector
from mysql.connector import errorcode
import dotenv
from dotenv import dotenv_values

# Load the .env file
secrets = dotenv_values(".env")

print(secrets)

try:
    connection = mysql.connector.connect(
        host='LAPTOP-ED96K4VM',
        database='movies',
        user='khilliard24',
        password='Stanle@3!',
    )

    if connection.is_connected():
        db_info = connection.get_server_info()
        print("Successfully connected to MySQL database")
        print(f"MySQL Server version: {db_info}")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")