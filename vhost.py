import os
import subprocess

domain = raw_input("Virtual domain: ")

www_folder = "/home/michael/www/"
vhost_filename = "/etc/nginx/sites-available/" + domain

template = open("vhost-laravel.conf", "r").read().replace("###ROOT###", www_folder + domain + "/public").replace("###DOMAIN###", domain)
virtual_host = open(vhost_filename, "w+")
virtual_host.write(template)

hosts = open("/etc/hosts", "a")
hosts.write("\n127.0.0.1 " + domain)

os.symlink(vhost_filename, vhost_filename.replace("sites-available", "sites-enabled"))

if not os.path.exists(www_folder + domain):
    os.makedirs(www_folder + domain)

subprocess.call("/etc/init.d/nginx restart", shell = True)