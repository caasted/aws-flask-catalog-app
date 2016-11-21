from routes.common import *

@app.route('/store/new/', methods=['GET', 'POST'])
def newStore():
	if not checkLogin():
		return redirect(url_for('showStores'))
	if request.method == 'POST':
		store = Store(name=request.form['name'], 
						user_id=login_session['user_id'])
		session.add(store)
		flash('New Store %s Successully Created!' % store.name)
		session.commit()
		return redirect(url_for('showCatalog', store_id=store.id))
	else:
		return render_template('newstore.html')
