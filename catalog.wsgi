#!/usr/bin/python
import sys
sys.path.insert(0,"/var/www/html/catalog/")

from catalog import app as application
application.secret_key = 'super_secret_key'
