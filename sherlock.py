from flask import Flask
from flask import g
from flask import Response
from flask import request
import json
import MySQLdb

app = Flask(__name__)

@app.before_request
def db_connect():
	g.conn = MySQLdb.connect(host='localhost',user='root',passwd='GroupTen',db='sherlock')
	g.cursor = g.conn.cursor()

@app.after_request
def db_disconnect(response):
	g.cursor.close()
	g.conn.close()
	return response

def userq(query, args=(), one=False):
	g.cursor.execute(query,args)
	rv = [dict((g.cursor.description[idx][0], value)
	for idx, value in enumerate(row)) for row in g.cursor.fetchall()]
	return (rv[0] if rv else None) if one else rv

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

@app.route('/userauthlogin',methods=['POST'])
def usercheck():
	req_json = request.get_json()
	e_mail = str(req_json['email'])
	g.cursor.execute("SELECT password FROM users WHERE email LIKE %s",([e_mail]))
	# g.cursor.execute("SELECT password FROM users WHERE email='gvk@gmail.com'")
	value = g.cursor.fetchone()
	passwd = value[0] 
	
	if (str(passwd) == str(req_json['password'])):
		userp = True
	else:
		userp = False
	result = {}
	result['userPresent'] = userp
	resp = Response(json.dumps(result),status=201,mimetype='application/json')
	return resp

@app.route('/registeruserprofile',methods=['POST'])
def register():
	req_json = request.get_json()
	g.cursor.execute("SELECT COUNT(email) FROM users where email LIKE %s",([str(req_json['email'])]))
	g.conn.commit()
	value = g.cursor.fetchone()
	value = value[0]
	res = False
	if (int(value) == 0):
		g.cursor.execute("INSERT INTO users(name,password,email,primarynumber,secondarynumber) VALUES (%s,%s,%s,%s,%s)",([str(req_json['name'])],[str(req_json['password'])],[str(req_json['email'])],[str(req_json['primarynumber'])],[str(req_json['secondarynumber'])]))
		g.conn.commit()	
		res = True
	result = {}
	result['registerUserProfile'] = res
	resp = Response(json.dumps(result),status=202,mimetype='application/json')
	return resp
	
@app.route('/data',methods=['GET'])
def show():
	result = userq("SELECT * FROM users")
	data = json.dumps(result)
	resp = Response(data,status=200,mimetype='application/json')
	return resp
	
if __name__ == '__main__':
  app.run()