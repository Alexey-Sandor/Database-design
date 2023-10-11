from sqlalchemy import Column, ForeignKey, Integer

from database import BaseModel


class BuyBook(BaseModel):
    __tablename__ = 'buy_book'

    id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.id'))
    book_id = Column(Integer, ForeignKey('book.id'))
    amount = Column(Integer)
