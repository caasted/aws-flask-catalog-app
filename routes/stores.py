from routes.common import *

@app.route('/')
@app.route('/store/')
def showStores():

	# Testing section to identify errors
	store = checkStore(1)

	stores = session.query(Store).order_by(asc(Store.id))

	if 'user_id' not in login_session:
		state = makeState()
		return render_template('publicstores.html', stores=stores, state=state)
	else:
		return render_template('stores.html', stores=stores)

