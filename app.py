from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from allen.allen import ValidInterval
from allen.allen import *
import json
import re
app = Flask(__name__)

from db_manager.db_manager import Database

db = Database()
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

@app.route('/before', methods=['POST','GET'])
def before():
  data = request.get_json()
  input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
  input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

  return str(is_before(input0,input1))

@app.route('/after' methods = ['POST', 'GET'])
def after():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_after(input0,input1))

@app.route('/equals', methods=['POST', 'GET'])
def equals():
    data = request.get_json()
    input0 = ValidInterval(data['values'][0]['start'], data['values'][0]['finish'])
    input1 = ValidInterval(data['values'][1]['start'], data['values'][1]['finish'])

    return str(is_equals(input0,input1))

