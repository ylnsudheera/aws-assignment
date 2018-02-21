from flask import Flask,render_template
app = Flask(__name__,static_url_path='')
from flask import request

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template(page_name)

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
