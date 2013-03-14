from flask import Flask, request, jsonify
from twython import Twython

app = Flask(__name__)

app_key = "Rrultq99nTcZ7yY4da8Iw"
app_secret="fSXA5q1w9GeAgAfx1GHt3L8lUmSMzUFowAPKYeo6Kwc"

@app.route("/login")
def login_url():

	t = Twython(
		app_key=app_key,
        app_secret=app_secret,
        callback_url=request.args['url']
	)
	
	auth_props = t.get_authentication_tokens()
	response = jsonify(auth_props)
	
	if (request.args['callback']):
		response.data = request.args['callback']+"("+response.data+")"
	
	return response


@app.route("/confirm")
def confirm_creds():
	
	t = Twython(
		app_key=app_key,
		app_secret=app_secret,
		oauth_token=request.args['oauth_token'],
		oauth_token_secret=request.args['oauth_token_secret']	
	)	
	
	auth_tokens = t.get_authorized_tokens()
	response = jsonify(auth_tokens)
	
	if (request.args['callback']):
		response.data = request.args['callback']+"("+response.data+")"
	
	return response


@app.route("/tweet")
def tweet():
	
	t = Twython(
		app_key=app_key,
		app_secret=app_secret,
		oauth_token=request.args['oauth'],
		oauth_token_secret=request.args['token']
	)
	
	status_update = t.updateStatus(status=request.args['status'])
	response = jsonify(status_update)
	
	if (request.args['callback']):
		response.data = request.args['callback']+"("+response.data+")"
	
	return response


if __name__ == "__main__":
   app.run()