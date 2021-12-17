import psycopg2

from dotenv import dotenv_values

CONFIG = dotenv_values(".env")


class DatabaseManager:
    postgre_connection = psycopg2.connect
    database_cursor = None

    def __init__(self, connection_database_name):
        self.postgre_connection = psycopg2.connect(dbname="postgres",
                                                   user=CONFIG["USER_NAME"],
                                                   password=CONFIG["PASSWORD_FOR_DATABASE"],
                                                   host=CONFIG["DATABASE_HOST_NAME"],
                                                   port=CONFIG["DATABASE_HOST_PORT"])
        self.database_cursor = self.postgre_connection.cursor()

    def get_person_by_hash(self, hash_code) -> int:
        self.database_cursor.exexute("""""")
        return 0

    def end_session(self):
        self.database_cursor.close()
        self.postgre_connection.close()


class DatabaseInitializer(DatabaseManager):
    postgre_connection = psycopg2.connect
    database_cursor = None
    database_name = str

    def __init__(self, connection_database_name):
        super().__init__(connection_database_name)
        self.postgre_connection = psycopg2.connect(dbname="postgres",
                                                   user=CONFIG["USER_NAME"],
                                                   password=CONFIG["PASSWORD_FOR_DATABASE"],
                                                   host=CONFIG["DATABASE_HOST_NAME"],
                                                   port=CONFIG["DATABASE_HOST_PORT"])
        self.database_cursor = self.postgre_connection.cursor()

        self.__create_new_table()

    def get_version_check(self):
        self.database_cursor.execute("SELECT version();")
        return self.database_cursor.fetchone()

    def add_column(self, column_name):
        pass

    def delete_current_table(self):
        creating_table_query = f"""DROP TABLE {self.database_name} RESTRICT"""
        self.database_cursor.execute(creating_table_query)
        self.postgre_connection.commit()

    def __create_new_table(self):
        self.database_name = "face_recognition_encoding"
        try:
            creating_table_query = f'''CREATE TABLE {self.database_name}
                                       (ID INT PRIMARY KEY NOT NULL,
                                       PERSON_FACE_MASK_ENCODING TEXT ); '''
            self.database_cursor.execute(creating_table_query)
            self.postgre_connection.commit()
        except psycopg2.errors.DuplicateTable:
            print("Table is already created somewhere... You, dumbass")
            self.postgre_connection.rollback()
        except psycopg2.errors.InFailedSqlTransaction:
            print("Table is already created somewhere... You, dumbass")
            self.postgre_connection.rollback()


if __name__ == "__main__":
    default_database_name = "postgres"
    face_recognition_database_initializer = DatabaseInitializer(default_database_name)
    face_recognition_database_initializer.delete_current_table()
    face_recognition_database_initializer.end_session()
