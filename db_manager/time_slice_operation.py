from db_manager.db_manager import Database
from db_manager.constants import *

db = Database()

def build_query(table_name, time):
    query = '''
        SELECT name, %s FROM %s
        WHERE start <= \'%s\'::date
        AND finish >= \'%s\'::date
    ''' % (table_name, table_name, time, time)
    return query

def time_slice_query(table_name, time):
    if table_name not in TABLE_NAMES:
        raise 'Invalid table name: %s' % table_name
    query = build_query(table_name, time)
    db.execute_sql(query)
    result = db.fetch_all()
    print('[executed] ', query)
    return result
