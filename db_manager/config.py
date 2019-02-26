import os


DATABASE_NAME = 'temporal_db'
HOST_NAME = 'localhost'
USERNAME = 'someone'
PASSWORD = 'password'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pdlcihuy'
