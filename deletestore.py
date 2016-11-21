from routes.common import *

@app.route('/store/<int:store_id>/delete/', methods=['GET', 'POST'])
def deleteStore(store_id):
	if not (checkLogin() and checkOwner(store_id)):
		return redirect(url_for('showStores'))
	store = checkStore(store_id)
	if not store:
		return redirect(url_for('showStores'))
	creator = checkUser(store.user_id)
	if not creator:
		return redirect(url_for('showStores'))
	if request.method == 'POST':
		session.delete(store)
		session.commit()
		flash('%s Successfully Deleted' % store.name)
		return redirect(url_for('showStores'))
	else:
		return render_template('deletestore.html', store=store)

