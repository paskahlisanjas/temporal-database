from db_manager.db_manager import Database

def build_querry_union(table_name, *args):
  query = 'SELECT %s FROM'