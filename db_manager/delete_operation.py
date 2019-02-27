TABLE_NAMES = ['salary', 'title']

def build_query(table_name, *args):
    query = 'DELETE FROM %s WHERE' % table_name
    iterator = 0
    for arg in args:
        if iterator % 2 == 0:
            query += ' %s %s \'%s\'' % (arg['attr'], arg['opr'], arg['val'])
        else:
            query += ' ' + arg
        iterator += 1
    query += ';'
    return query

def delete_record(table_name, *args):
    if table_name not in TABLE_NAMES:
        raise 'Invalid table name: %s' % table_name
    query = build_query(table_name, *args)
    print(query)
