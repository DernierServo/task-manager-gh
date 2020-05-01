from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
	user_ip = request.remote_addr
	return f'hello world from DServo labs, your IP is {user_ip}'

if __name__ == '__main__':
	hello()
