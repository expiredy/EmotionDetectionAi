import psycopg2

from dotenv import load_dotenv
load_dotenv(".env")


conn = psycopg2.connect(dbname='database', user='db_user',
                        password='mypassword', host='localhost')

cursor = conn.cursor()