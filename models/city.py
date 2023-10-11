from sqlalchemy import Column, Integer, String

from database import BaseModel


class City(BaseModel):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name_city = Column(String)
    days_delivery = Column(Integer)
