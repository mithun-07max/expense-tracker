EXPENSE TRACKER - REBUILT PROJECT
=================================

This rebuild contains the changes made to the project:
- Django authentication: login/register/logout
- Expense CRUD: add/edit/delete
- User-specific expenses
- Total expense card
- Number of expenses card
- Average expense card
- Category-wise doughnut chart
- Monthly expense bar chart
- Recent expenses table
- Colorful responsive dashboard
- Colorful glass-style login/register pages
- Bootstrap 5
- Bootstrap Icons
- Chart.js
- SQLite database

PROJECT STRUCTURE
-----------------
expense_tracker/
    manage.py
    requirements.txt

    expense_tracker/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py

    expenses/
        __init__.py
        apps.py
        models.py
        forms.py
        views.py
        urls.py
        admin.py

    templates/
        base.html
        dashboard.html
        add_expense.html
        edit_expense.html
        login.html
        register.html

    static/
        css/
            style.css
            auth.css


SETUP
-----
1. Open PowerShell in this project folder.

2. Install Django:
   pip install -r requirements.txt

3. Create migrations:
   python manage.py makemigrations

4. Apply migrations:
   python manage.py migrate

5. Optional: create admin account:
   python manage.py createsuperuser

6. Start the server:
   python manage.py runserver

7. Open:
   http://127.0.0.1:8000/


IMPORTANT
---------
The Chart.js dashboard uses json_script.
The views.py file therefore passes normal Python lists:
category_labels
category_values
monthly_labels
monthly_values

Do not use json.dumps() for these four context values.
