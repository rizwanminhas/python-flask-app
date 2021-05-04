# About
A simple app which saves html form data in a postgres db and then sends an email using the Mailtrap's free account.

This app uses Python, Flask, Postgres, PgAdmin, Mailtrap and bunch of other dev dependencies.

## Local setup
Install the pipenv for virtual environment:
`pip install pipenv`
and then `pipenv shell`

Install all the dependencies in pipenv:
`pipenv install flask psycopg2 psycopg2-binary flask-sqlalchemy gunicorn`

Start postgres and pgadmin via docker compise:
`docker-compose up`

Start the app via pipenv:
`pipenv shell` and then `python app.py`, the app will start on `http://127.0.0.1:5000`



## Troubleshooting
1. If you see error messages like `pipenv shell already activated` or `Shell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated` then try the following solution:
  
   - `exec bash`
   - `pipenv shell` (takes you to the virtual environment, default python is 3.x)
   - `python app.py` (execute the app)

2. If PgAdmin is not able to connect to the Postgres then make sure for the postgres server host name you are using the same name that is used inside the `docker-compose.yml` file, this is because both pgadmin and postgres are running in the Docker. But the app itself should use `localhost` while connecting to the postgres.

## Random notes

1. To see installed python packages use `pip3 freeze`

2. To check which version of python `pipenv` is using do this:
```
    pipenv shell
    python (will be python 3.x)
    import sys
    sys.executable
    quit()
```

3. To check what packages are used in pipfile `pipenv lock -r`

4. To install a package in pipenv `pipenv install camelcase` and to install a dev dependency use `pipenv install camcelcase --dev`

5. To install packages from `requirements.txt` use `pipenv install -r ./requirements.txt`

6. To check for security and vulnerabilities use `pipenv check`

7. To check dependency graph use `pipenv graph`

8. When it comes to deployment:
    - You want to use the lock file so use `pipenv lock`
    - On your deployment server use `pipenv install --ignore-pipfile`

9. you can also run pipenv commands without being in the shell e.g. `pipenv run python` (runs the python from within the pipenv).

10. You can also create tables from python... From the pipenv python prompt execute `from app import db` and then `db.create_all()`.