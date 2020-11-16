from flask import Flask
from flask import make_response 

app = Flask(__name__)

@app.route('/')
def home():
	return "<h1>Hello</h1>"

# @app.route('/<page_name>')
# def other_page(page_name):
# 	return make_response('the page named %s does not exist.' % page_name, 404)



if __name__ == '__main__':
	app.run(debug=True)






