# aws-flask-catalog-app
Rewriting the catalog application to run on an AWS Linux server and use PostgreSQL for data storage

## Server Configuration Steps
1. Create a new user named "grader" with the command `adduser grader`, follow prompts
2. Add "grader" to the sudoers group by creating a new file `nano /etc/sudoers.d/grader`
..* Enter the file contents `grader ALL=(ALL) NOPASSWD:ALL` and save
3. Update all currently instlaled packages using `apt-get update` then `apt-get upgrade`
4. Change the SSH port from 22 to 2200 by editing `/etc/ssh/sshd_config` using nano
..* Change the line below "What ports, IPs and protocols we listen for" from `Port 22` to `Port 2200`
5. Configure the Uncomplicated Firewall to only allow incoming connections for SSH, HTTP, and NTP
..1. Verify UFW is currently disabled with the command `ufw status`; if not disabled: `ufw disable`
..2. `ufw default deny incoming`
..3. `ufw default allow outgoing`
..4. `ufw allow 2200/tcp` (the modified SSH port)
..5. `ufw allow www` (http)
..6. `ufw allow ntp`
..7. `ufw enable`
..8. Confirm UFW is now running and properly configured with the command `ufw status`
6. Verify the server's timezone is set to UTC by running the command `timedatectl`
..* If the timezone is not UTC: `nano /etc/timezone` and change the contents to `Etc/UTC`
7. Install apache with the command `apt-get install apache2`
8. Install the required library with the command `apt-get install libapache2-mod-wsgi`
9. Configure the apache service using `nano /etc/apache2/sites-enabled/000-default.conf`
..* Add the following lines at the bottom of the file, before `</VirtualHost>`
```
	WSGIDaemonProcess catalog user=catalog group=catalog threads=5
	WSGIScriptAlias / /var/www/html/catalog/myapp.wsgi

	<Directory /var/www/html/catalog>
		WSGIProcessGroup catalog
		WSGIApplicationGroup %{GLOBAL}
		Order deny,allow
		Allow from all
	</Directory>
	
10. Restart the apache service with the command `apache2ctl restart`
