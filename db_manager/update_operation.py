from db_manager.db_manager import Database

CSV_DELIMITER = ','
COLUMNS_DELIMITER = ', '

TABLE_NAMES = ['salary', 'title']
SALARY_COLUMNS = ['name', 'salary', 'start', 'finish']
TITLE_COLUMNS = ['name', 'title', 'start', 'finish']

db = Database()

def build_query_update(table_name, *args):
    query = 'UPDATE %s SET current = false WHERE' % table_name
    for arg in args:
        if arg['type'] == 'condition':
            query += ' %s %s \'%s\'' % (arg['attr'], arg['opr'], arg['val'])
        else:
            query += ' ' + arg['opr']
    query += ';'
    return query

def update_record(table_name, *args):
    if table_name not in TABLE_NAMES:
        raise 'Invalid table name: %s' % table_name
    query = build_query_update(table_name, *args)
    db.execute_sql(query)
    print('[executed] ', query)

def build_querry_insert(table_name, *args):
  stringify = lambda val : '\'%s\'' % val
  columns_join = lambda table : COLUMNS_DELIMITER.join(SALARY_COLUMNS if table == SALARY_TABLE else TITLE_COLUMNS)
  insert_sql = lambda table, row : 'INSERT INTO %s (%s) VALUES (%s)' % (table, columns_join(table), COLUMNS_DELIMITER.join(map(stringify, row)))

