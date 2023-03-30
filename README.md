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

# REST API Endpoints 

## Employees

### Get a list of all employees
```bash
GET /employees/
```

This endpoint returns a paginated list of all employees in the system.

Optional query parameters:

- page - The page number to retrieve. Defaults to 1.
- page_size - The number of items per page. Defaults to 100.
- sort - The field to sort the list by. Prefix with - to sort in descending order.
- search - A search string to filter the list by the first and last name.

Also, the endpoint allows filtering based on specific fields of the model. Example:
```shell
GET /employees/?first_name="Jhon"
```

```shell
GET /employees/?industry="IT"
```

### CRUD Operation on Employee

The API supports the CRUD operations on the employees

Get an employee:
```shell
GET /employees/<id>
```

Create an employee:
```shell
POST /employees/create 
```
Body example:

```python
body = {
    'id': 1,
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john@example.com',
    'gender': 'Male',
    'date_of_birth': '1990-01-01',
    'industry': 'IT',
    'salary': 50000.0,
    'years_of_experience': 3.0,
    'others': {},
}
```

Update an employee:
```shell
PUT /employees/<id>/update 
```
Body example:

```python
body = {
    'id': 1,
    'first_name': 'John',
    'last_name': 'Doe',
    'email': 'john@example.com',
    'gender': 'Male',
    'date_of_birth': '1990-01-01',
    'industry': 'IT',
    'salary': 50000.0,
    'years_of_experience': 3.0,
    'others': {},
}
```

Delete an employee:
```shell
DELETE /employees/<id>/delete 
```

### Analytical endpoints

```shell
GET analytical/employees-average-age-per-industry
```

```shell
GET analytical/employees-average-salary-per-industry
```

```shell
GET analytical/employees-average-salary-per-years-of-experience
```

```shell
GET analytical/employees-average-salary-per-gender
```

```shell
GET analytical/analytical/employees-average-age-per-gender
```

