# RegPro
COMP 3700 project

Dependencies:
astroid==2.3.3
click==7.1.1
colorama==0.4.3
Flask==1.1.2
Flask-Login==0.5.0
Flask-SQLAlchemy==2.4.1
Flask-WTF==0.14.3
isort==4.3.21
itsdangerous==1.1.0
Jinja2==2.11.1
lazy-object-proxy==1.4.3
MarkupSafe==1.1.1
mccabe==0.6.1
pylint==2.4.4
pylint-flask==0.6
pylint-flask-sqlalchemy==0.2.0
pylint-plugin-utils==0.6
six==1.14.0
SQLAlchemy==1.3.16
typed-ast==1.4.1
Werkzeug==1.0.1
wrapt==1.11.2
WTForms==2.2.1

How to add a page:
1) Go to routes.py and copy the /home route all the way to the return statement (3 lines of code)
2) Paste this at the bottom of routes and add name of your page as the new route and change the function name to match
3) Create your html document in templates (Note: Flask allows for inheritance, so you can reuse html code)