TABLE_NAMES = ['salary', 'title']

def delete_record(table_name, **kwargs):
    if table_name not in TABLE_NAMES:
        raise 'Invalid table name!'
    query = 'DELETE '
