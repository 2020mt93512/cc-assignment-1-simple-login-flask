from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/home')
def do_home():
	return render_template('home.html')

@app.route('/')
def do_default_redirect():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return redirect('/home')

@app.route('/login', methods=['GET'])
def redirect_login():
	return redirect('/')

@app.route('/logout', methods=['GET'])
def redirect_logout():
	return redirect('/')

@app.route('/login', methods=['POST'])
def do_login():
	session['wrong_username'] = False
	session['wrong_password'] = False
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True
		return redirect('/home')
	else:
		session['logged_in'] = False
		if request.form['username'] != 'admin':
			session['wrong_username'] = True
		if request.form['password'] != 'password':
			session['wrong_password'] = True
		return redirect('/')

@app.route('/logout', methods=['POST'])
def do_logout():
	session['wrong_username'] = False
	session['wrong_password'] = False
	session['logged_in'] = False
	return redirect('/')

if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(debug=True,host='0.0.0.0', port=4000)