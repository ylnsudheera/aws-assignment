from flask import Flask
app = Flask(__name__)
from flask import request

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/save_employee')
def save_employee():
	import MySQLdb
	reply = "success"
	conn = MySQLdb.connect(host= "aws-assignment.cdggmmymki0w.ap-south-1.rds.amazonaws.com",
                  user="sudheera",
                  passwd="sudheera123",
                  db="Employee")
	x = conn.cursor()
	name = request.args.get('name')
	age = request.args.get('age')
	query = "INSERT INTO emp(name,age) values('"+name+"',"+str(age)+")"
	try:
		x.execute(query)
		conn.commit()
	except Exception:
		print("error")
		conn.rollback()
		reply= "failed, please try again..."

	conn.close()
	return reply

#port = 5000 #+ random.randint(0, 999)
url = "0.0.0.0"
app.run(host=url,port=8080,debug=False)
