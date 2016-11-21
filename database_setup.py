from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from models.base import Base
from models.user import User
from models.store import Store
from models.product import Product

engine = create_engine('postgresql://catalog:catalog@localhost:8000/catalog')
Base.metadata.create_all(engine)
