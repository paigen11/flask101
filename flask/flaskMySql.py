from flask import Flask, render_template
from flaskext.mysql import MySQL 

app = Flask(__name__)
# create an instance of the MySQL class
mysql = MySQL()
# add to the app (Flask object) some config data for our connection
app.config['MYSQL_DATABASE_USER'] = 'x'

app.config['MYSQL_DATABASE_PASSWORD'] = 'x'
# the name of the database we want to connect to at the database server
app.config['MYSQL_DATABASE_DB'] = 'restaurants_db'
# where the MYSQL server is at
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
# use the mysql object's method 'init_app' and pass it the flask object
mysql.init_app(app)

@app.route("/", methods = ['GET'])
def index():
# set up a cursor object, which is what the sql object uses to connect and run queries
	cursor = mysql.connect().cursor()
# execute a query with the execute method
	cursor.execute("SELECT name, category, image, id FROM restaurant WHERE 1")
# turn the mysql object into something we can use
	data = cursor.fetchall()
	if data is None:
		return "Your query returns no results"
	else:
		return render_template('rest.html',
			data = data)

@app.route('/reviews/<id>', methods = ['GET'])
def info(id):
	cursor = mysql.connect().cursor()
	cursor.execute("SELECT restaurant.name, reviews.stars, reviews.title, reviews.review, users.name FROM restaurant JOIN reviews ON restaurant.id = reviews.restaurant_id JOIN users ON reviews.a_id = users.id WHERE restaurant.id = %s" % id)		
	data = cursor.fetchall()
	if data is None:
		return "Your query returns no results"
	else:
		return render_template('restaurant.html',
			data = data)

if __name__ == "__main__":
	app.run(debug=True)