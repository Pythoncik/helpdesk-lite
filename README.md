# HelpDesk Lite

A small IT helpdesk web application built with Python and Django.

## Features
- User registration, login and logout
- Personal support tickets
- Categories, priorities and statuses
- Search and filtering
- SQLite database and Django ORM
- Django Admin
- JSON endpoint: `/api/tickets/`
- Automated tests

## Run
```powershell
python -m venv venv
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe manage.py migrate
venv\Scripts\python.exe manage.py runserver
```
Open `http://127.0.0.1:8000/register/`.

## Portfolio
**HelpDesk Lite — Django Web Application**

A web-based IT helpdesk system developed with Python and Django. Includes authentication, ticket management, filtering, SQLite database integration, Django Admin and a JSON endpoint.
