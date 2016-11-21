from sqlalchemy import Column, Integer, String

from models.base import Base

class User(Base):
	__tablename__ = 'user'
	__table_args__ = {'sqlite_autoincrement': True}

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
