# aws-flask-catalog-app
Rewriting the catalog application to run on an AWS Linux server and use PostgreSQL for data storage

## Server Information
**IP Address:** `35.163.10.3`
**URL:** `ec2-35-163-10-3.us-west-2.compute.amazonaws.com`

## Server Configuration Steps

1. Create a new user named "grader" with the command `adduser grader`, follow prompts
  * Locally create a key pair for "grader" and paste the public key at `/home/grader/.ssh/authorized_keys`
2. Add "grader" to the sudoers group by creating a new file `nano /etc/sudoers.d/grader`
  * Enter the file contents `grader ALL=(ALL) PASSWD:ALL` and save
3. Update all currently installed packages using `apt-get update` then `apt-get upgrade`
4. Change the SSH port and disable root login using `nano /etc/ssh/sshd_config`
  * Change the line below "What ports, IPs and protocols we listen for" from `Port 22` to `Port 2200`
  * In the Authentication section, replace `PermitRootLogin without-password` with `PermitRootLogin no`
  * Implement these changes with the command `service ssh restart`
  * **Note:** If you disconnect after this step you will only be able to reconnect to the server via SSH as "grader". If so, you will need to use `sudo` to complete many of the remaining steps.
5. Configure the Uncomplicated Firewall to only allow incoming connections for SSH, HTTP, and NTP
  1. Verify UFW is currently disabled with the command `ufw status`; if not disabled: `ufw disable`
  2. `ufw default deny incoming`
  3. `ufw default allow outgoing`
  4. `ufw allow 2200/tcp` (the modified SSH port)
  5. `ufw allow www` (http)
  6. `ufw allow ntp`
  7. `ufw enable`
  8. Confirm UFW is now running and properly configured with the command `ufw status`
6. Verify the server's timezone is set to UTC by running the command `timedatectl`
  * If the timezone is not UTC: `nano /etc/timezone` and change the contents to `Etc/UTC`
7. Install apache with the command `apt-get install apache2`
8. Install the required library with the command `apt-get install libapache2-mod-wsgi`
9. Configure the apache service using `nano /etc/apache2/sites-enabled/000-default.conf`
  * Add the following lines at the bottom of the file, before `</VirtualHost>`
  ```
  	WSGIDaemonProcess catalog user=catalog group=catalog threads=5
  	WSGIScriptAlias / /var/www/html/catalog/catalog.wsgi

  	<Directory /var/www/html/catalog>
  		WSGIProcessGroup catalog
  		WSGIApplicationGroup %{GLOBAL}
  		Order deny,allow
  		Allow from all
  	</Directory>
  ```
10. Create a new user named "catalog" with the command `adduser catalog`, follow prompts
11. Implement the changes with the command `apache2ctl restart`
12. Install pip with the command `apt-get install python-pip`
13. Add the python package SQLAlchemy using `python -m pip install SQLAlchemy`
14. Add the python package Flask using `python -m pip install flask`
15. Add the python package oauth2client using `python -m pip install oauth2client`
16. Install git with the command `apt-get install git`
17. Clone the catalog git respository into the correct directory with the following steps:
  1. `cd /var/www/html`
  2. `git clone https://github.com/caasted/aws-flask-catalog-app.git catalog`
18. Install PostgreSQL using `apt-get install postgresql`
19. Create a user and database named "catalog" in PostgreSQL
  1. `su postgres`
  2. `cd`
  3. `psql`
  4. `CREATE USER catalog WITH PASSWORD 'catalog';`
  5. `CREATE DATABASE catalog WITH OWNER = catalog;`
  6. `\q`
  7. `exit`
20. Install required support packages:
  1. `apt-get install python-psycopg2`
  2. `apt-get install libpq-dev`
21. Initialize the database with `python /var/www/html/catalog/database/database_setup.py`
22. Populate the database using the command `python /var/www/html/catalog/database/database_fill.py`
23. Verify the application is [online](http://ec2-35-163-10-3.us-west-2.compute.amazonaws.com/)
