# Temporal Database

## Pre-installation

The dependencies bellow should already be installed in the system:

1. PostgreSQL

  Follow [these instructions](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04) for more detailed installation.

## Installation

(Currently tested only on Ubuntu 16.04)

1. Clone the repository
  ```
  git clone git@github.com:paskahlisanjas/temporal-databse.git
  ```
2. Change directory `cd temporal-database`

3. <b>(optional)</b> Consider creating virtual environment to localize the development environment
  ```
  pip3 install virtualenv --user
  python3 -m virtualenv env
  ```
  activate the `virtualenv` by typing `source env/bin/activate`, and deactivate it with `deactivate` command.

4. Change directory to django main project `cd temporaldb`

5. Install all the dependencies
  ```
  pip install -r requirements.txt
  ```

6. Run django server
  ```
  python manage.py runserver
  ```
  server is now by default available on `http://localhost:8000`.
