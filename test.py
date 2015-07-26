
# imported the Flask class
from flask import Flask, url_for, request, jsonify, make_response, json
# create an instance of this class. first argument is the name of the application's module or package
app = Flask(__name__)

from pusher import Pusher
p = Pusher(
	app_id='131763',
	key='f7159e9e2eea1dda351b',
	secret='ff5fc82451faa0f65a33',
	ssl=True,
	port=443
)



# we then use route() decorator to tell Flask what URL should trigger our function
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		payload = request.get_json()
		message = payload[u'message']
		
		p.trigger(u'private-test-channel', u'voila', {u'some': message})
		
		return jsonify({'message': message})
	else:
		return 'hello'


@app.route("/auth", methods=['POST'])
def pusher_authentication():

  auth = p.authenticate(
    channel=request.form['channel_name'],
    socket_id=request.form['socket_id']
  )
  return json.dumps(auth)


@app.route('/hello')
def hello():
	return 'Hello World'


# # Variable rules example

# show the user profile for that user
@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username

# show the post with the given id, the id is an integer
@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()
	


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

# # URL Building
# @app.route('/profile/<username>')
# def profile(username):
# 	pass

# with app.test_request_context():
# 	print (url_for('profile', username = 'John Doe'))






# Finally we use the run() function to run the local server with our application. The

if __name__ == "__main__": 
	app.debug = True
	app.run()
# makes sure the server only runs if the script is executed directly from the Python interpreter and not used as an imported module
