from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from db_manager.delete_operation import delete_record
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

    delete_record(table, *operations)

    return 'jsonify(salaries)'
