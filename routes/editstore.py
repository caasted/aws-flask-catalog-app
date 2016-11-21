from routes.common import *

@app.route('/store/<int:store_id>/edit/', methods=['GET', 'POST'])
def editStore(store_id):
	if not (checkLogin() and checkOwner(store_id)):
		return redirect(url_for('showStores'))
	store = checkStore(store_id)
	if not store:
		return redirect(url_for('showStores'))
	if request.method == 'POST':
		if request.form['name']:
			store.name = request.form['name']
			session.add(store)
			session.commit()
			flash('Store "%s" Succcessfully Edited' % store.name)
			return redirect(url_for('showCatalog', store_id=store_id))
	else:
		return render_template('editstore.html', store=store)

