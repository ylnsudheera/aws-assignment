#Server Connection to MySQL:

import MySQLdb
conn = MySQLdb.connect(host= "aws-assignment.cdggmmymki0w.ap-south-1.rds.amazonaws.com",
                  user="sudheera",
                  passwd="sudheera123",
                  db="Employee")
x = conn.cursor()
name = "bala"
age = 22
query = "INSERT INTO emp(name,age) values('"+name+"',"+str(age)+")"
try:
	x.execute(query)
	conn.commit()
except Exception:
	print("error")
	conn.rollback()

conn.close()