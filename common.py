from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from flask import session as login_session
import random
import string

from models.base import Base
from models.user import User
from models.store import Store
from models.product import Product

app = Flask(__name__)

engine = create_engine('sqlite:///productcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# DB query helper functions
def checkStore(store_id):
    result = session.query(Store).filter_by(id=store_id).first()
    if not result:
        flash("Store ID doesn't exist!")
    return result

def checkProduct(product_id):
    result = session.query(Product).filter_by(id=product_id).first()
    if not result:
        flash("Product ID doesn't exist!")
    return result

def checkUser(user_id):
    result = session.query(User).filter_by(id=user_id).first()
    if not result:
        flash("User ID doesn't exist!")
    return result

# Permissions helper functions
def checkLogin():
    if 'user_id' not in login_session:
        flash("Please log in with your Google+ account to make changes.")
        return None
    return True

def checkOwner(store_id):
    store = checkStore(store_id)
    owner = checkUser(store.user_id)
    if owner.id != login_session['user_id']:
        flash("You don't have permission to edit that store or its products.")
        return None
    return True

# User helper functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session['email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).first()
    return user.id

def getUserID(email):
    user = session.query(User).filter_by(email=email).first()
    if not user:
        return None
    return user.id

# Create anti-forgery state token
def makeState():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return state

