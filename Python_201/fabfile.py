from fabric.api import sudo,env,roles,execute,put,run, local, lcd,prompt, cd,parallel

def UpdateServer():
	sudo("yum -y upgrade",pty=True)
"""
This example uses python Fabric to deploy
mysql/mariadb and apache
"""
#import the os module to get file basenames
import os

# define groups of webservers and databases
env.roledefs = {
	"webserver" : ["ec2-54-183-135-106.us-west-1.compute.amazonaws.com"],
	"database" : ["ec2-54-183-135-106.us-west-1.compute.amazonaws.com"]
}

# define a special group called all so we can easily sendout commands to all servers
env.roledefs["all"] = [h for r in env.roledefs.values() for h in r]

# the packages that are required to run our application on the server group
packages_required = {
	"webserver" : [ "httpd", "php" ,"ntp", "php-mysqli" ],
	"database" : ["mariadb-server"]
}

# Download any files as required

@roles("database") # this decorator will make the fn follow it run all database group server
def install_database():
	sudo ("yum -y install %s" % "".join(packages_required["database"]),pty=True)
	# active Mysql/Mariadb
	sudo("systemctl enable mariadb",pty=True)
	sudo("systemctl start mariadb",pty=True)
	sudo(r""" mysql -h 127.0.0.1 -u root -e "CREATE USER 'web'@'%' IDENTIFIED BY 'web'; GRANT ALL PRIVILEGES ON *.* TO 'web'@'%';FLUSH PRIVILEGES;" """)
	run("ps -ef | grep mysql")

@parallel
@roles("database")
def setup_database():
	tmpdir = "/tmp"
	print("Thers is no way to download files. Just skipping it...")

@roles("webserver")
def install_webserver():
	sudo ("yum -y install %s" % " ".join(packages_required["webserver"]),pty=True)	
        sudo("systemctl enable httpd.service",pty=True)
        sudo("systemctl start httpd.service",pty=True)

	sudo("setsebool -P httpd_can_network_connect=1",pty=True)
	sudo("setsebool -P httpd_read_user_content=1",pty=True)
	
def deploy():
	#execute(install_database)
	execute(install_webserver)
