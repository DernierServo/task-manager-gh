from uuid import uuid4

class Config:
	secret_key = str(uuid4())
	#app.config['SECRET_KEY'] = secret_key
	SECRET_KEY = secret_key

