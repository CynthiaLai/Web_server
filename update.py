import cgi, cgitb 
import sqlite3

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

conn = sqlite3.connect('age.db')
cur = conn.cursor()

# Get data from fields
name = form.getvalue('name')
age  = form.getvalue('age')
cur.execute("UPDATE Age set age = %s where name = '%s'" % (age, name))

print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Update CGI Program</title>"
print "</head>"
print "<body>"
cur.execute('SELECT * FROM Age')  
while True:
			row = cur.fetchone()
			if row == None:
				break
			print "<h1>%s %s</h1>" % (row[0],row[1])
print "<a href= /index.html >login</a>"
print "</body>"

conn.commit()
conn.close()
