# Temporal Database

(Currently tested only on Ubuntu 16.04)

## Pre-installation

The program needs PostgreSQL to run appropriately. Follow instructions bellow to install PostgreSQL.

```
$ sudo apt-get update
$ sudo apt-get install postgresql
```

## Installation

1. Clone the repository
  ```
  $ git clone git@github.com:paskahlisanjas/temporal-databse.git
  ```
2. Change directory `cd temporal-database`

3. <b>(optional)</b> Consider creating virtual environment to localize the development environment
  ```
  $ pip3 install virtualenv --user
  $ python3 -m virtualenv env
  ```
  activate the `virtualenv` by typing `source env/bin/activate`, and deactivate it with `deactivate` command.

4. Install all the dependencies
  ```
  $ pip install -r requirements.txt
  ```

5. Run flask server
  ```
  $ FLASK_APP=app.py FLASK_DEBUG=1 flask run
  ```
  server is now by default available on `http://localhost:5000`.

To be able to simulate the cases, the database created should be populated first.

1. Login, create database, and create user
  ```
  $ sudo -u postgres psql
  postgres=# CREATE DATABASE temporal_db;
  postgres=# CREATE USER someone WITH ENCRYPTED PASSWORD 'password';
  postgres=# GRANT ALL PRIVILEGES ON DATABASE temporal_db TO someone;

  ```
2. Populate database
  ```
  $ cd db_manager && python populate_db.py
  ```
