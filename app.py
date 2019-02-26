from models import UpdateForm, UnionForm
from flask import Flask
from flask import render_template, flash, redirect, url_for
from db_manager.db_manager import Database
from db_manager.config import Config
import psycopg2

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

@app.route('/union', methods=['GET'])
def union():
  union = UnionForm()