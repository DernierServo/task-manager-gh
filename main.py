from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)
todos = ['Read books', 'Cook the dinner', 'Study for an exam']

@app.route('/')
def index():
	user_ip = request.remote_addr
	response = make_response(redirect('/hello'))
	response.set_cookie('user_ip', user_ip)

	return response


@app.route('/hello')
def hello():
	user_ip = request.cookies.get('user_ip')
	context = {
		'user_ip': user_ip,
		'todos': todos,
	}

	return render_template('hello.html', **context)
	#return render_template('hello.html', user_ip = user_ip)


if __name__ == '__main__':
	hello()