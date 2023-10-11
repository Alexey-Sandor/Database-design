from sqlalchemy import Column, ForeignKey, Integer, String

from database import BaseModel


class Book(BaseModel):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    price = Column(Integer)
    amount = Column(Integer)
