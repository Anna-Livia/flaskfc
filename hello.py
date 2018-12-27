from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('homepage.html')

@app.route('/hello')
def hello_world():
	return "hello world!"

@app.route('/user/<username>')
def get_user_profile(username):
	# show the user profile for that user
    return 'User %s' % username

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath
