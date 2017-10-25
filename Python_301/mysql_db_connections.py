# Prior to this need to install MySQL-python rpm
import MySQLdb
conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="")
c = conn.cursor()
c.execute("CREATE DATABASE testdb")
c.execuet("USE testdb")
c.execute("CREATE TABLE users (username VARCHAR(50), email VARCHAR(50)) ")
userlist = [('paul','pdomain.com'),('donny','ddomain.com')]
c.executemany("INSERT INTO users VALUES (%s,%s)",userlist)
conn.commit()
c.execute("SELECT * FROM users")

# fetching the values using a for loop
for row in c.fetchall():
	print row
conn.close()
