from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
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

    db = Database()
    db.execute_sql('SELECT * FROM salary')
    salaries = db.fetch_all()

    # db.execute_sql('SELECT * FROM title')
    # titles = db.fetch_all()
    # return render_template(
    #     'delete.html',
    #     salaries=salaries,
    #     titles=titles
    # )
    return jsonify(salaries)
