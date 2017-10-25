import sqlite3 # default db module available with python
conn = sqlite3.connect('dem3d.db') # here is the db doesn't exist the database is created
c = conn.cursor() # cursor is a handle to execute our queries
c.execute('''CREATE TABLE users(username text,email text)''')
c.execute("INSERT INTO users VALUES ('Sam', 'me@mydomain.com')")
conn.commit()

# Inserting values through variable 
username, email = 'I', 'I@idomain.com' # Assigning multiple variables
c.execute("INSERT INTO users VAlUES(?, ?)",(username, email))
conn.commit()
# Inserting values as List
userlist = [('paul', 'p@domain.com'),('donny', 'd@domain.com')]
c.executemany("INSERT INTO users VAlUES(?, ?)",userlist)
conn.commit()

# Select using username as variable
c.execute('SELECT email from users where username = ?',(username,))
print c.fetchone()

# Lookup with single value in tuple
lookup = ('Sam',)
c.execute('SELECT email from users where username = ?', lookup)
print c.fetchone()



