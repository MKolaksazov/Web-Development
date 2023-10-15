# Web-Development
Development of web applications, sites, hosting etc.

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

Go to: http://localhost/joomla/administrator (the control panel)

----

# III) How to install the LAMP stack under Linux 
(not recommended)
