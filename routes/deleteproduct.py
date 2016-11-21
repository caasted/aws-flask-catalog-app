from routes.common import *

@app.route('/store/<int:store_id>/catalog/<int:product_id>/delete/', 
			methods=['GET', 'POST'])
def deleteProduct(store_id, product_id):
	if not (checkLogin() and checkOwner(store_id)):
		return redirect(url_for('showStores'))
	store = checkStore(store_id)
	if not store:
		return redirect(url_for('showStores'))
	creator = checkUser(store.user_id)
	if not creator:
		return redirect(url_for('showStores'))
	product = checkProduct(product_id)
	if not product:
		return redirect(url_for('showStores'))
	if request.method == 'POST':
		session.delete(product)
		session.commit()
		flash('Product "%s" Successfully Deleted' % (product.name, ))
		return redirect(url_for('showCatalog', store_id=store_id))
	else:
		return render_template('deleteproduct.html', store_id=store_id, 
								product=product)

