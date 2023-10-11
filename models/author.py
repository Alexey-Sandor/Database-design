from sqlalchemy import Column, Integer, String

from database import BaseModel


class Author(BaseModel):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    name_author = Column(String)
