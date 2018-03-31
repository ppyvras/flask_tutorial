# flask_tutorial
My version of the [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## the virtual environment

Virtual environment is called flaskapp, probably should have called venv per convention

$ source flaskapp/Scripts/activate # for windows when using GitBash

## setting up environment variable

$ export FLASK_APP=microblog.py (or use set on windows when not using bash)

## running the app

$ flask run

App then available locally at:

http://localhost:5000/

## database migrations

Uses flask-migrate which integrates flask with alembic

$ flask db init  # initialising the migration

$ flask db migrate -m "<desc of migration>"

$ flask db upgrade  # follow through with migration plan
