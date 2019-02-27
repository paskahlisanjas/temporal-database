from db_manager.db_manager import Database
from db_manager.constants import *
from db_manager.delete_operation import delete_record

db = Database()

stringify = lambda val : '\'%s\'' % val
columns_join = lambda table : COLUMNS_DELIMITER.join(SALARY_COLUMNS if table == SALARY_TABLE else TITLE_COLUMNS)
insert_sql = lambda table, row : 'INSERT INTO %s (%s) VALUES (%s);' % (table, columns_join(table), COLUMNS_DELIMITER.join(map(stringify, row)))

def sort_row(table_name, row_dict):
    row_dict['current'] = '1'
    if table_name == SALARY_TABLE:
        return [row_dict[item] for item in SALARY_COLUMNS]
    return [row_dict[item] for item in TITLE_COLUMNS]

def build_query(table_name, value):
    sorted_row = sort_row(table_name, value)
    query = insert_sql(table_name, sorted_row)
    return query

def insert_record(table_name, value):
    if table_name not in TABLE_NAMES:
        raise 'Invalid table name: %s' % table_name
    query = build_query(table_name, value)

    delete_arg_condition = {
        'type': 'condition',
        'attr': 'name',
        'opr': '=',
        'val': value['name']
    }
    delete_arg_operator = {
        'type': 'operator',
        'opr': 'AND',
    }
    delete_arg_current = {
        'type': 'condition',
        'attr': 'current',
        'opr': '=',
        'val': '1'
    }

    row_count = delete_record(table_name, delete_arg_current, delete_arg_operator, delete_arg_condition)

    db.execute_sql(query)
    row_count += db.row_count()
    db.commit()
    print('[executed] ', query)

    return row_count
