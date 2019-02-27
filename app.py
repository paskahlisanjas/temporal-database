from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from db_manager.delete_operation import delete_record
from db_manager.insert_operation import insert_record
from allen.allen import ValidInterval
from allen.allen import *
import json
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

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
  data = request.get_json()

  table = data['table']
  operations = tuple(data['operations'])

  update_operation(table, *operations)

  return 'jsonify(salaries)'

@app.route('/union', methods=['POST'])
def union():
  data = request.get_json()

  table = data['table']
  operations = tuple(data['operations'])

  update_operation(table, *operations)

  return 'jsonify(salaries)'

@app.route('/before', methods=['POST'])
def before():
  data = request.get_json()
  input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
  input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

  return str(is_before(input0,input1))

@app.route('/after', methods = ['POST'])
def after():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_after(input0,input1))

@app.route('/equals', methods=['POST'])
def equals():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_equals(input0,input1))

@app.route('/during', methods=['POST'])
def during():
  data = request.get_json()
  input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
  input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

  return str(is_during(input0,input1))

@app.route('/contains', methods=['POST'])
def contains():
  data = request.get_json()
  input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
  input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

  return str(is_contains(input0,input1))

@app.route('/starts', methods=['POST'])
def starts():
  data = request.get_json()
  input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
  input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

  return str(is_starts(input0,input1))

@app.route('/startby', methods=['POST'])
def startby():
  data = request.get_json()
  input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
  input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

  return str(is_started_by(input0,input1))

@app.route('/finishes', methods=['POST'])
def finishes():
  data = request.get_json()
  input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
  input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

  return str(is_finishes(input0,input1))

@app.route('/finishedby', methods=['POST'])
def finishedby():
  data = request.get_json()
  input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
  input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

  return str(is_finished_by(input0,input1))

@app.route('/meets', methods=['POST'])
def meets():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_meets(input0,input1))

@app.route('/met_by', methods=['POST'])
def met_by():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_met_by(input0,input1))


@app.route('/overlaps', methods=['POST'])
def overlaps():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_overlaps(input0,input1))


@app.route('/overlapped_by', methods=['POST'])
def overlapped_by():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_overlapped_by(input0,input1))


@app.route('/finishes', methods=['POST'])
def finishes():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_finishes(input0,input1))

@app.route('/finished_by', methods=['POST'])
def finished_by():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_finished_by(input0,input1))
