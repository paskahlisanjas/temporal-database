from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from db_manager.delete_operation import delete_record
from db_manager.insert_operation import insert_record
import json
import re
app = Flask(__name__)

from db_manager.db_manager import Database

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/delete', methods=['POST'])
def delete():
    data = request.get_json()

    table = data['table']
    operations = tuple(data['operations'])

    row_affected = delete_record(table, *operations)

    return 'Row affected: %s' % row_affected

@app.route('/insert', methods=['POST'])
def insert():
    data = request.get_json()

    table = data['table']
    value = tuple(data['value'])

    row_affected = insert_record(table, *value)

    return 'Row affected: %s' % row_affected
