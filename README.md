# Django-API

## Setup

1. Install and enter the virtual environment using [poetry](https://python-poetry.org/docs/)
```shell
poetry install
poetry shell
```

2. Create the `.env` file
```shell
cp dev_ops/.env.template .env
```

Edit this file with your preferred credentials (or you can leave it as it is).

3. Start the DB process using [docker-compose](https://docs.docker.com/compose/)
```shell
docker-compose -f dev_ops/dockercompose.yml up
```

4. Check DB connection is ok:
```shell
python manage.py shell 
```

## Migrations
To apply migrations use:
```shell
python manage.py migrate 
```

Optional: populate the DB with the initial employee data
```
python manage.py populate_db
```

## Run
To start the server use:
```shell
python manage.py runserver
```


## Tests
To run the tests use: 
```shell
python manage.py test api.tests 
```
