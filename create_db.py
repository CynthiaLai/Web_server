import sqlite3
conn = sqlite3.connect('age.db')

c = conn.cursor()

# Create table
c.execute('''CREATE TABLE Age
             (name, age)''')

# Insert a row of data
c.execute("INSERT INTO Age VALUES ('Marry','20')")
c.execute("INSERT INTO Age VALUES ('John','22')")

# Save (commit) the changes
conn.commit()

conn.close()
