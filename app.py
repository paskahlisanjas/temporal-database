from models import UpdateForm, UnionForm
from flask import Flask
from flask import render_template, flash, redirect, url_for, request
from db_manager.db_manager import Database
from db_manager.config import Config
import psycopg2
import psycopg2.extras
import json

app = Flask(__name__)
app.config.from_object(Config)

db = Database()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_form', methods=['GET'])
def updateform():
    salary = db.execute_sql('SELECT * FROM salary;')
    salary = db.fetch_all()
    querry = UpdateForm()
    # if querry.validate_on_submit():
    #   flash('UPDATE {} SET {} WHERE {}'.format(
    #           querry.table.data, querry.values.data, querry.condition.data))
    #   return render_template('update.html', salary = salary, querry = querry)
    return render_template('update.html', salary = salary, querry = querry)

@app.route('/update', methods=['POST'])
def update():
  salary = db.execute_sql('SELECT * FROM salary;')
  salary = db.fetch_all()
  querry = UpdateForm()
  if querry.validate_on_submit():
    db.execute_sql('{}'.format(querry.update.data))
    flash('{}'.format(querry.update.data))
    return render_template('update.html', salary = salary, querry = querry)

@app.route('/union_form', methods=['GET'])
def unionform():
  union = UnionForm()
  return render_template('union.html', union = union)

@app.route('/union', methods=['POST'])
def union():
  union = UnionForm()
  if union.validate_on_submit():
    result_union = db.execute_sql('SELECT {} FROM {} UNION (SELECT {} FROM {})'.format(
      union.select1.data,union.table1.data,union.select2.data,union.table2.data))
    result_union = db.fetch_all()
    return render_template('result_union.html', result_union = result_union)

@app.route('/cobaupdate', methods=['POST'])
def cobaupdate():
    data = request.get_json(silent=True)

    table = data['table']
    updated_values = data['values']
    update_condition = data['condition']

    # res = db.update(table, updated_values, update_condition)
    

    return json.dumps(res)