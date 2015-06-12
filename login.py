# Import modules for CGI handling 
import cgi, cgitb 
import sqlite3

user_list = ['user1','user2']
pass_list = ['0000','0001']

conn = sqlite3.connect('age.db')
cur = conn.cursor()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
usrname = form.getvalue('usrname')
password  = form.getvalue('password')


print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Hello - Second CGI Program</title>"
print "</head>"

for i in range(len(user_list)):
	if (usrname == user_list[i]) and (password == pass_list[i]):
		print "<body>"
		print "<h2>Hello %s </h2>" % (usrname)
		cur.execute('SELECT * FROM Age')    

		print "<form action= %s method= %s>" %("/cgi-bin/update.py", "post")
		while True:
			row = cur.fetchone()
			if row == None:
				break
			print "<h1>%s %s</h1>" % (row[0],row[1])
		print "name:<input type= %s name= %s ><br>" % ("text","name")
		print "age:<input type= %s name= %s ><br>" % ("text","age")
		print "<input type=%s value= %s></form>" % ("submit","update")
		print "<a href= /index.html >Logout</a>"
		print "<a href= /data.html >Add Data</a>"
		break
		print "</body>"
	elif i == len(user_list)-1 :
		print "<body>"
		print "<h2>Error user </h2>"
		print "<a href= /index.html >login</a>"
		print "</body>"
	
conn.close()
