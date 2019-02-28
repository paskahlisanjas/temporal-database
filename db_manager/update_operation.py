from db_manager.db_manager import Database
from db_manager.select_operation import select_record
from db_manager.insert_operation import insert_record
from db_manager.delete_operation import delete_record
from db_manager.constants import *

def update_existing(table_name, update, val):
    expression = {}
    columns = SALARY_COLUMNS if table_name == SALARY_TABLE else TITLE_COLUMNS
    for column, value in zip(columns, val[1:]):
        expression[column] = value
    for item in update:
        expression[item['attr']] = item['val']
    row_affected = insert_record(table_name, expression)
    return row_affected

def update_record(table_name, update, *operations):
    current_arg_operator = {
        'type': 'operator',
        'opr': 'AND',
    }
    current_arg_condition = {
        'type': 'condition',
        'attr': 'current',
        'opr': '=',
        'val': '1'
    }
    result = select_record(table_name, *operations, current_arg_operator, current_arg_condition)

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
    row_affected = delete_record(table_name, *operations, delete_arg_operator, delete_arg_current)

    row_affected += update_existing(table_name, update, result[0])
    return row_affected
