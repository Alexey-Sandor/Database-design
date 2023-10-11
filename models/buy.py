from sqlalchemy import Column, ForeignKey, Integer, Text

from database import BaseModel


class Buy(BaseModel):
    __tablename__ = 'buy'

    id = Column(Integer, primary_key=True)
    buy_description = Column(Text)
    client_id = Column(Integer, ForeignKey('client.id'))
