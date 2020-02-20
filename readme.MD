# PROJECTED AWARDS
---

## Author 
---

**Anthony Ng'ang'a**

---
## Project Description
---
This is a Django Web App similar to the Awwwards website. A user can create an account, login and post projects for others to rate. You also get reviews on your projects. This application also has an API where you can connect to two endpoints, the user and projects endpoints. You can view the site here:

---
## Technologies Used
---

- PYTHON
- DJANGO
- POSTMAN API TESTING
- POSTGRES DATABASE
- BOOTSTRAP AND CSS
- HTML MARKDOWN

---
### Installing
---
​
A step by step series of examples that tell you how to get a development env running
​
1. set up a virtual environment using the following command
​
```
python3.7 -m venv --without-pip virtual
```
​
And activate it
​
```
source virtual/bin/activate
```
1. install the latest version of pip
​
```
curl https://bootstrap.pypa.io/get-pip.py | python
```
​
1. Install the requirements in the requirements.txt file using
```
pip install -r requirements.txt
```
1. create a .env file in your rootfolder and add the following configurations
```
SECRET_KEY='<random-string>'
DEBUG=True
ALLOWED_HOSTS='*'
DATABASE_URL='postgres://databaseowner:password@localhost/databasename'
```
1. create postgres database
```
CREATE DATABASE <your-database-name>
```
1. create a migration using the following command
```
python3.7 manage.py makemigrations
```
​
and migrate
```
python3.7 manage.py migrate
```
1. create a admin account
```
python 3.7 manage.py createsuperuser
```
and add your credentials
​
1. run the application using 
```
python3.7 manage.py runserver
```
1. navigate to the admin panel by typing 
```
localhost:8000/admin
```
​
---
## API
---
This application provides an API for users and projects. The endpoints to the API are:

- users - https://projecteda.herokuapp.com/api/users
- users - https://projecteda.herokuapp.com/api/projects

---
## Project live-link
---

https://projecteda.herokuapp.com/

---
## Licence
---

The MIT License (MIT)

Copyright (c) 2020 Anthony Ng'ang'a

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contacts Information

- You can reach me at any time using : - ngash.anto@gmail.com

