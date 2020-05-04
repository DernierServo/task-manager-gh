from flask import Flask, request, make_response, redirect, render_template, session, url_for
from flask_bootstrap import Bootstrap
from uuid import uuid4
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField	#Import fields
from wtforms.validators import DataRequired


app = Flask(__name__)
secret_key = str(uuid4())
app.config['SECRET_KEY'] = secret_key
bootstrap = Bootstrap(app)
todos = ['Read books', 'Cook the dinner', 'Study for an exam']


class LoginForm(FlaskForm):
	username = StringField('User name', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Send')

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
		return redirect(url_for('index'))

	return render_template('hello.html', **context)



if __name__ == '__main__':
	hello()