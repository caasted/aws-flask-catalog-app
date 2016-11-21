from flask import jsonify

from routes.common import *

# JSON APIs to view Store and Product Information
@app.route('/store/JSON')
def storeJSON():
    stores = session.query(Store).all()
    return jsonify(stores=[s.serialize for s in stores])

@app.route('/store/<int:store_id>/catalog/JSON')
def catalogJSON(store_id):
    store = checkStore(store_id)
    products = session.query(Product).filter_by(
        store_id=store_id).all()
    return jsonify(Product=[p.serialize for p in products])

@app.route('/store/<int:store_id>/catalog/<int:product_id>/JSON')
def productJSON(store_id, product_id):
    item = checkProduct(product_id)
    return jsonify(Product=item.serialize)

