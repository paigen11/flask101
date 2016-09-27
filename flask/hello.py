from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    print "Hello World!"
    return "Hello, World!"

@app.route('/algorithm')
def results():
	def centered_average(new_list):
		new_list.sort()
		del new_list[0]
		new_list.pop()
		if new_list[0] == new_list[1]:
			del new_list[0]
		center_value = sum(new_list) / len(new_list)
		return center_value
	print centered_average([1,2,3,4,100])	
	return str(centered_average([1,2,3,4,100]))

@app.route('/login')
def login():
	return render_template('login.html', 
		name= 'Paige',
		title = 'Ninja Assassin',
		a_list = [1,2,5, 3, 9],
		a_dict = {
			'boy1': "Mike TV",
			'boy2': "Augustus Glute"
		},
		wannabetitle = 'Super Hero Billionaire')	

@app.errorhandler(404)
def page_missing(e):
	print e
	return redirect('/', 404)

@app.route('/user/<user_name>')
def user_page(user_name):
	return 'user %s' % user_name				    

if __name__ == "__main__":
    app.run(debug=True)