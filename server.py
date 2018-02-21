from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/save_employee')
def save_employee():
    return 
#port = 5000 #+ random.randint(0, 999)
url = "0.0.0.0"
app.run(host=url,port=8080,debug=False)
