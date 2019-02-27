import psycopg2
from db_manager.config import *

class Database:
    def __init__(self):
        self.connect()

    def connect(self):
        self.database = psycopg2.connect(
            user=USERNAME,
            password=PASSWORD,
            host=HOST_NAME,
            database=DATABASE_NAME
        )
        self.cursor = self.database.cursor()

    def execute_sql(self, query):
        self.cursor.execute(query)
        self.database.commit()

    def fetch_all(arg):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.database.close()
