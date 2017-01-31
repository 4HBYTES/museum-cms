# Museum CMS

This is a dummy CMS for a proof of concept, it is definitely not production ready.

## How to run:

### SQL

 * `create user cms with password 'cms';`
 * `create database cms;`
 * `grant all privileges on database cms to cms;`

### Python

 * `virtualenv env` # You may need the `-p` switch to precise __python 2__ here (no need for mac)
 * `source env/bin/activate`
 * `pip install -r requirements.txt`
 * You will need to run this command the first time: `python manage.py migrate`
 * `python manage.py runserver`

### Admin

 * `python manage.py createsuperuser`

## Environment variables

 * `DATABASE_NAME: String` Name of the psql database
 * `DATABASE_USER: String` Name of the psql user
 * `DATABASE_PASSWORD: String` Password of the psql user
 * `DATABASE_HOST: Strign` Domain/Ip of the psql database
 * `DATABASE_PORT: Integer` Port of the psql database
 * `DEBUG: Boolean` Should be False in production


## Curl examples

### Signup (first_name and last_name are optional)

`curl http://127.0.0.1:8000/users/signup --data '{"email": "toto@test.com", "password": "123456", "first_name": "Toto", "last_name": "Test"}' -v`

 * 201 {} OK
 * 409 {'error': 'xxx'} email already exists

### Signin

`curl http://127.0.0.1:8000/users/signin --data '{"email": "toto@test.com", "password": "123456"}' -v`

 * 200 {} OK
 * 401 {} email does not exists/password is incorrect

### Profile

`curl http://127.0.0.1:8000/users/profile -H 'AUTHORIZATION: Basic dG90b0B0ZXN0LmNvbToxMjM0NTY=' -v`

 * 200 {id,email,first_name,last_name} OK

### Password

`curl http://127.0.0.1:8000/users/password -X PUT --data '{"password": "654321"}' -H 'AUTHORIZATION: Basic dG90b0B0ZXN0LmNvbToxMjM0NTY=' -`

 * 200 {} OK

### All products

`curl http://127.0.0.1:8000/products/ -v`

 * 200 [{id,name,description,price,currency}] OK

### One products (by its uuid)

`curl http://127.0.0.1:8000/products/8f1e4151-61f1-4275-8135-c40e795e5dd9 -v`

 * 200 {id,name,description,price,currency} OK
 * 404 Not found

### All news (no pagination)

`curl http://127.0.0.1:8000/media/news -v`

 * 200 [{id, created_at, name, description}] OK

### All events (no pagination)

`curl http://127.0.0.1:8000/media/events -v`

 * 200 [{id, place, date, name, description}] OK

### Create ticket(s)

`curl http://127.0.0.1:8000/ticket/create --data '{"token": "3d008cb7-15ce-4e30-b5d1-b626064797fc", "quantity": 1, "product_id": "3e855fad-dd92-4545-96e1-40fb5dfd8eab", "user_id": "78112ad2-cf3c-4b82-9200-7debaf4a7740"}' -v`

 * 201 {} OK

### Use a ticket

`curl http://127.0.0.1:8000/ticket/use --data '{"token": "3d008cb7-15ce-4e30-b5d1-b626064797fc", "ticket_id": "b9797f1d-24e0-432f-8fa7-81aead71a985"}' -v`

 * 200 {} OK
 * 404 {} cannot find the ticket
 * 409 {} ticket already used
