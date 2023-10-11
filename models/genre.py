from sqlalchemy import Column, Integer, String

from database import BaseModel


class Genre(BaseModel):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name_genre = Column(String)
