from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from uuid import uuid4


app = Flask(__name__)
secret_key = str(uuid4())
app.config['SECRET_KEY'] = secret_key
bootstrap = Bootstrap(app)
todos = ['Read books', 'Cook the dinner', 'Study for an exam']


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


@app.route('/hello')
def hello():
	user_ip = session.get('user_ip')
	context = {
		'user_ip': user_ip,
		'todos': todos,
	}

	return render_template('hello.html', **context)
	#return render_template('hello.html', user_ip = user_ip)


if __name__ == '__main__':
	hello()