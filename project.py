from routes.common import *
from routes.stores import showStores
from routes.newstore import newStore
from routes.editstore import editStore
from routes.deletestore import deleteStore
from routes.catalog import showCatalog
from routes.product import showProduct
from routes.newproduct import newProduct
from routes.editproduct import editProduct
from routes.deleteproduct import deleteProduct
from routes.getjson import storeJSON, catalogJSON, productJSON
from routes.gconnect import gconnect
from routes.gdisconnect import gdisconnect

if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=8000)
