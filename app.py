from flask import Flask, session, redirect, url_for, escape, request, render_template, g
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app=Flask(__name__)
app.secret_key=b'abbas'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TutorApp.db'
db = SQLAlchemy(app)



# given a query, executes and returns the result
# (don't worry if you don't understand this code)
def query_db(query, args=(), one=False):
    cur = db.engine.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.route('/', methods=['GET', 'POST'])
def home():
	if 'username' in session:
		return redirect(url_for('index'))
	else:
		return render_template('signup.html')

@app.route('/home', methods = ['GET', 'POST'])
def index():
	if 'username' in session:
		# index.html is the home page after login
		return render_template('index.html')
	else:
		# home.html is the home page before login
		return render_template('home.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    items = []
    if 'username' in session:
        return redirect(url_for('home'))
    elif request.method == 'GET':
        return render_template('signup.html')
    else:
        firstname = '"' + request.form['firstname'] + '"'
        lastname = '"' + request.form['lastname'] + '"'
        # username = '"' + request.form['username'] + '"'
        password = '"' + request.form['password'] + '"'
        confirmedpass = '"' + request.form['confirmedpass'] + '"'
        email = '"' + request.form['email'] + '"'
        phone = '"' + request.form['txtEmpPhone'] + '"'
        securityans = '"' + request.form['securityans'] + '"'
        myQuery = "SELECT * FROM Tutors where firstName is " + '"' + request.form['firstname'] + '"'
        insert_Query = "INSERT INTO Tutors (firstName, lastName, password, confirmedPassword, phone, securityAnswer, email) values(" + firstname + "," + lastname + ',' + password + ',' + confirmedpass + ',' + phone + ',' + securityans + ',' + email + ')' 
        results = db.engine.execute(text(myQuery))
        for item in results:
            items.append(item)
        if len(items) > 0:
        	taken = "username already taken"
        	return render_template('signup.html', taken=taken)
        else:
        	if False:
        		pass
	        	'''
	        	if request.form['firstname'] == "" or request.form['lastname'] == "" or request.form['username'] == "" or request.form['password'] == "":
	        		empty = "please make sure all fields are filled"
	        		return render_template('instructorSignup.html', empty=empty)
	        	# Another case you want to take care of, is special characters including underscores
	        	elif not (request.form['username'].isalnum()):
	        		right_values = """ Please make sure that there are special characters in your username
	        		including underscores"""
	        		return render_template('student-signup.html', right_values = right_values)
	        	# Check to make sure no numbers are entered for firstname, last name and not all
				# characters in username are numbers
	        	elif not ( request.form['firstname'].isalpha() and request.form['lastname'].isalpha() and not request.form['username'].isdigit()):
	        		right_values = """Please make sure you enter alphanumeric characters for your Firstname and Lastname.
	        		with no spaces and usernmames cannot be all numbers"""
	        		empty = ''
	        		return render_template('instructorSignup.html', empty=empty, right_values = right_values)
	        	'''
        	else:
	            results = db.engine.execute(text(insert_Query))
	            global instructor_username
	            instructor_username = request.form['firstname']
	            session['username']= request.form['firstname'], 'Tutor'
	            return redirect(url_for('home'))



@app.route('/debug', methods = ['GET', 'POST'])
def debug():
	return render_template('sample.html', random=random)


if __name__=="__main__":
	app.run(debug=False)