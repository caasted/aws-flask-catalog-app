from flask import make_response
import json
import httplib2


from routes.common import *

# Disconnect - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session['access_token']
    if access_token is None:
    	response = make_response(json.dumps('Current user not connected.'), 401)
    	response.headers['Content-Type'] = 'application/json'
    	return response
    url = ('https://accounts.google.com/o/oauth2/revoke?token=%s' 
    											% login_session['access_token'])
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        del login_session['access_token'] 
    	del login_session['gplus_id']
    	del login_session['username']
    	del login_session['email']
        del login_session['user_id']
        del login_session['state']
    	# response = make_response(json.dumps('Successfully disconnected.'), 200)
    	# response.headers['Content-Type'] = 'application/json'
    	# return response
    	flash("Successfully logged out.")
    	return redirect(url_for('showStores'))
    else:
    	response = make_response(json.dumps(
    							'Failed to revoke token for given user.', 400))
    	response.headers['Content-Type'] = 'application/json'
    	return response


