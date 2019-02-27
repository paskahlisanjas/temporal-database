from db_manager.db_manager import Database
from db_manager.constants import *

db = Database()

def build_query(table_name, *args):
    query = 'SELECT * FROM %s WHERE' % table_name
    for arg in args:
        if arg['type'] == 'condition':
            query += ' %s %s \'%s\'' % (arg['attr'], arg['opr'], arg['val'])
        else:
            query += ' ' + arg['opr']
    query += ';'
    return query

def select_record(table_name, *args):
    if table_name not in TABLE_NAMES:
        raise 'Invalid table name: %s' % table_name
    query = build_query(table_name, *args)
    db.execute_sql(query)
    result = db.fetch_all()
    print('[executed] ', query)
    return result
