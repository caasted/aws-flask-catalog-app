from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base
from models.user import User

class Store(Base):
	__tablename__ = 'store'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		"""Return store type object data in easily serializeable format"""
		return {
			'id': self.id, 
			'name': self.name, 
			'user_id': self.user_id, 
		}
