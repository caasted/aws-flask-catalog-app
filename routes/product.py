from routes.common import *

@app.route('/store/<int:store_id>/catalog/<string:category>/<int:product_id>/')
def showProduct(store_id, category, product_id):
	store = checkStore(store_id)
	if not store:
		return redirect(url_for('showStores'))
	creator = checkUser(store.user_id)
	if not creator:
		return redirect(url_for('showStores'))
	product = checkProduct(product_id)
	if not product:
		return redirect(url_for('showStores'))
	categories = session.query(Product).filter_by(store_id=store_id).group_by(
						Product.category).with_entities(Product.category).all()
	if 'user_id' not in login_session or (creator.id != 
													login_session['user_id']):
		state = makeState()
		return render_template('publicproduct.html', store=store, 
													creator=creator, 
													categories=categories, 
													product=product, 
													state=state)
	else:
		return render_template('product.html', store=store, 
												creator=creator, 
												categories=categories, 
												product=product)

