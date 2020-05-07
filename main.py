from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from app.forms import LoginForm

import unittest
from app import create_app

app = create_app()

todos = ['Read books', 'Cook the dinner', 'Study for an exam']


@app.cli.command()
def test():
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
	return render_template('500.html', error=error)


@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	session['user_ip'] = user_ip
	return response


@app.route('/hello', methods=['GET', 'POST'])
def hello():
	user_ip = session.get('user_ip')
	login_form = LoginForm()
	username = session.get('username')
	context = {
		'user_ip': user_ip,
		'todos': todos,
		'login_form': login_form,
		'username': username,
	}

	#Detecta cuando se envía un método Post y luego valida la forma
	if login_form.validate_on_submit():
		username = login_form.username.data
		#guardando el username en la sesion:
		session['username'] = username
		flash('User name was registered successfully!')
		return redirect(url_for('index'))

	return render_template('hello.html', **context)



if __name__ == '__main__':
	hello()