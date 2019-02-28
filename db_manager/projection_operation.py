from db_manager.db_manager import Database
from db_manager.constants import *
from db_manager.coalescer import *

from datetime import datetime

db = Database()

def format_columns(columns):
    return COLUMNS_DELIMITER.join(columns + ['start', 'finish'])

def build_query(table_name, columns, *args):
    query = 'SELECT %s FROM %s WHERE' % (format_columns(columns), table_name)
    for arg in args:
        if arg['type'] == 'condition':
            query += ' %s %s \'%s\'' % (arg['attr'], arg['opr'], arg['val'])
        else:
            query += ' ' + arg['opr']
    query += ';'
    return query

def project_record(table_name, columns, *args):
    if table_name not in TABLE_NAMES:
        raise 'Invalid table name: %s' % table_name
    query = build_query(table_name, columns, *args)
    db.execute_sql(query)
    result = db.fetch_all()
    print('[executed] ', query)
    return tune_result(result, columns)
