## This is a excercise project about the web framework with the language Python, 'Django'.
-----

Here, you will find help information and sample code about:

1) Installing and working with Django under Linux

2) Installing and setting-up Apache and Xampp (the combined Apache, php and mySQL) under Linux
(for this lookup in the previous directory)

3) A sample blog site under Django

4) Various other projects

   Have a nice time!

----

# I) Install Django

## 1) install pip (after XAMPP installation the name is python3, pip3)

```$ sudo apt-install python3-venv python3-pip```

Test

```
$ python3
>>> import django
>>> print(django.get.version())

(4.1)
```
(version 4.1 runs python 3.8)

## 2) start a new project

```$ mkdir directoryname``` (make new directory where the project will be located)

```$ django-admin startproject new_project_name```

```$ python3 manage.py runserver``` or ```$ python3 manage.py runserver 8001``` (if you want to be on a different port e.g. 8001)

test: http://localhost:8000 (or http://127.0.0.1:8000)

## 3) make new app

```$ django-admin startapp new_app_name```

Structure of the project and app(s):
```
new_project_name/----+
                     +--- new_project_name/--+
                     |                       +--- __init__.py
                     |                       +--- settings.py
                     |                       +--- urls.py
                     |                       +--- wsgi.py
                     +--- new_app_name/--+
                     |                   +--- static/
                     |                   +--- templates/
                     |                   +--- migrations/
                     |                   |
                     |                   +--- admin.py 
                     |                   +--- apps.py
                     |                   +--- models.py 
                     |                   +--- test.py 
                     |                   +--- urls.py 
                     |                   +--- views.py
                     |
                     +--- manage.py
```
You can follow the tutorial on the django documentation site `My very first project`
Go to: https://docs.djangoproject.com/en/4.2/

----

# II) Connecting Django to mySQL

## 1) Connecting Django to mySQL

Inside the directory of the project with the same name there is other directory and indside the fire settings.py

```/new_project_name/new_project_name/settings.py```

Inside this file the DATABASES parameters should be changed to the mySQL parameters: 

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database_name',
        'USER': 'username',
        'PASSWORD': password
        'HOST': 'localhost',
        'PORT': '3306',
        # navigate to the correct directory
        'OPTIONS': {
            'read_default_file': '/opt/lampp/etc/my.cnf',
        },
    }
}
```

the OPTIONS parameter gives the correct directory to the my.cnf file (because it was not explicitly named!)

Also, you should make a database with the same name inside the 'phpMyAdmin' control panel (at 127.0.0.1/dashboard)

## 2) 

Inside the same settings.py file you should insert the new app every time a new app is created:

```
INSTALLED_APPS = [
   'django.contrib.admin',
...
...
...

   'new_app_name.apps.New_app_nameConfig',
]
```
The new line, that should be added have to include the name of the new app, 'dot' apps 'dot' and again the name with capital first letter and Config appended to the name immediately afterwards.

----

# III) Make migrations 
(migrations are made every time a change has been performed in the models.py file in order to implement those changes into the SQL database)

## 1)

```$ python3 manage.py migrate```

It should perform an output:

"Applying ***.0001 ...OK" or something like this

## 2) For the implementation of the models inside the SQL:

```$ python3 manage.py makemigrations new_app_name```

The output should contain a number at the end, such as 0001

```$ python3 manage.py sqlmigrate new_app_name 0001```

Finally:

```$ python3 manage.py migrate```

## 3) Creating a superuser

```$ python3 manage.py createsuperuser```
(It is very important to migrate before making superuser, otherwise the user won't be available under the mySQL and you won't be able to enter even the admin control panel)

