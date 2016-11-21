from routes.common import *

@app.route('/store/<int:store_id>/catalog/<int:product_id>/edit/', 
			methods=['GET', 'POST'])
def editProduct(store_id, product_id):
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
		if request.form['name']:
			product.name = request.form['name']
		if request.form['category']:
			product.category = request.form['category']
		if request.form['description']:
			product.description = request.form['description']
		if request.form['price']:
			product.price = request.form['price']
		session.add(product)
		session.commit()
		flash('Product "%s" Successfully Edited' % (product.name, ))
		return redirect(url_for('showProduct', store_id=store_id, 
												category=product.category, 
												product_id=product.id))
	else:
		return render_template('editproduct.html', store_id=store_id, 
								product=product)

