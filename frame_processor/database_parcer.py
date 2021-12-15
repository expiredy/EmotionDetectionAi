import psycopg2

from dotenv import dotenv_values


config = dotenv_values(".env")

database_name = "database"

conn = psycopg2.connect(dbname=database_name, user=config["USER_NAME"],
                        password=config["PASSWORD_FOR_DATABASE"], host='localhost')

cursor = conn.cursor()