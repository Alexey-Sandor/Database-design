from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import BaseModel


class Client(BaseModel):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    name_client = Column(String)
    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship('City', back_populates='client')
    email = Column(String)
