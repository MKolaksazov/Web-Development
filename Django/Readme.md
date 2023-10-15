## This is a excercise project about the web framework with the language Python, 'Django'.
-----

Here, you will find help information and sample code about:

1) Installing and working with Django under Linux

2) Installing and setting-up Apache and Xampp (the combined Apache, php and mySQL) under Linux

3) A sample blog site under Django

4) Various other projects

   Have a nice time!

----

# I) How to install and setup the `XAMPP` stack service under Linux

## 1) Install XAMPP

```$ sudo apt install net-tools```

go to: https://www.apachefriends.org/download.html

64 bit php (?? version)

make the file executable

```$ sudo chmod 755 xampp-linux-x64-7.2.34-0-installer.ras```

```$ sudo ./xampp-linux-x64-7.2.34-0-installer.ras```

Install!!! Test!!!

How to check:

go to: http://localhost/dashboard

## 2) Set password for mySQL / Entering the mySQL console /

Turn on the mySQL from the panel or the console:

```$ sudo /opt/lampp/lampp startmysql```

!!! (because the file ```mysql.sock``` won't be in the ```/opt/lampp/var/mysql``` directory)

```$ sudo /opt/lampp/bin/mysql -h localhost -u root -p```

enter pwd:

(shell)MariaDB>

----

# II) Install Joomla!

## 1) 

Turn on (start) the XAMPP panel

Go to: joomla.org

Download the zip file

Go to: /opt/lampp/htdocs/ mkdir joomla (or other suitable name)

Go to: /opt/lampp/htdocs/joomla/ and place there the zip file

Extract the zip file there

```$ sudo chmod -R 777 /opt/lampp/htdocs/joomla```

http://localhost/joomla

Installation

http://localhost/joomla/administrator (the control panel)

----

# III) Install Django

## 1) install pip (after XAMPP installation the name is python3, pip3)

```$ sudo apt-install python3-venv python3-pip```

Test

```$ python3
>>> import django
>>> print(django.get.version())

(4.1)
```
(version 4.1 runs python 3.8)

## 2) start a new project

```$ mkdir directoryname``` (make new directory where the project will be located)

```$ django-admin startproject new_project_name```

```$ python3 manage.py runserver```

test: http://localhost:8000 (or http://127.0.0.1:8000)

## 3) make new app

```$ django-admin startapp new_app_name```

Structure of the project and app(s):

/new_project_name----+
                     +---/new_project_name---+
                     |                       +--- __init__.py
                     |                       +--- settings.py
                     |                       +--- urls.py
                     |                       +--- wsgi.py
                     +---/new_app_name---+
                     |                   +---/static
                     |                   +---/templates
                     |                   +---/migrations
                     |                   |
                     |                   +--- admin.py 
                     |                   +--- apps.py
                     |                   +--- models.py 
                     |                   +--- test.py 
                     |                   +--- urls.py 
                     |                   +--- views.py
                     |
                     L manage.py
----

# IV) How to install the LAMP stack under Linux (not recommended)
