from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from db_manager.time_slice_operation import time_slice_query
from db_manager.delete_operation import delete_record
from db_manager.insert_operation import insert_record
from db_manager.select_operation import select_record
from allen.allen import ValidInterval
from allen.allen import *
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

@app.route('/update', methods=['POST'])
def update():
  data = request.get_json()

  table = data['table']
  operations = tuple(data['operations'])

  update_operation(table, *operations)

  return 'jsonify(salaries)'

@app.route('/time-slice', methods=['POST'])
def time_slice():
  data = request.get_json()
  table = data['table']
  time = data['time']

  result = time_slice_query(table, time)
  print(result)
  return jsonify(result)

@app.route('/select', methods=['POST'])
def select():
    data = request.get_json()

    table = data['table']
    operations = tuple(data['operations'])

    result = select_record(table, *operations)
    return jsonify(result)

@app.route('/union', methods=['POST'])
def union():
  data = request.get_json()

  table = data['table']
  operations = tuple(data['operations'])

  update_operation(table, *operations)

  return 'jsonify(salaries)'

@app.route('/before', methods=['POST','GET'])
def before():
  data = request.get_json()
  input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
  input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

  return str(is_before(input0,input1))
