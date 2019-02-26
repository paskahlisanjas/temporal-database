import psycopg2
import csv
from db_manager import Database

SALARY_DIR = 'data/salary.csv'
TITLE_DIR = 'data/title.csv'

CSV_DELIMITER = ','
COLUMNS_DELIMITER = ', '

SALARY_TABLE = 'salary'
TITLE_TABLE = 'title'

CREATE_TABLE_SALARY = 'CREATE TABLE IF NOT EXISTS %s (id SERIAL PRIMARY KEY,  name VARCHAR (6), salary INTEGER, start DATE, finish DATE, current BOOLEAN);' % SALARY_TABLE
CREATE_TABLE_TITLE = 'CREATE TABLE IF NOT EXISTS %s (id SERIAL PRIMARY KEY,  name VARCHAR (6), title VARCHAR (3), start DATE, finish DATE, current BOOLEAN);' % TITLE_TABLE

SALARY_COLUMNS = ['name', 'salary', 'start', 'finish', 'current']
TITLE_COLUMNS = ['name', 'title', 'start', 'finish', 'current']

def insert_csv(dir, table):
    with open(dir, newline='') as file:
        rows = csv.reader(file, delimiter=CSV_DELIMITER)
        next(rows, None)
        for row in rows:
            query = insert_sql(table, row)
            print('Executing %s' % query)
            db.execute_sql(query)

stringify = lambda val : '\'%s\'' % val
columns_join = lambda table : COLUMNS_DELIMITER.join(SALARY_COLUMNS if table == SALARY_TABLE else TITLE_COLUMNS)
insert_sql = lambda table, row : 'INSERT INTO %s (%s) VALUES (%s)' % (table, columns_join(table), COLUMNS_DELIMITER.join(map(stringify, row)))

db = Database()

db.execute_sql(CREATE_TABLE_SALARY)
print('Table `salary` has been created.')

db.execute_sql(CREATE_TABLE_TITLE)
print('Table `title` has been created.')

insert_csv(SALARY_DIR, SALARY_TABLE)
insert_csv(TITLE_DIR, TITLE_TABLE)

db.close()
print('---------------------- DONE :)')
