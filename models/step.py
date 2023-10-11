from sqlalchemy import Column, Integer, String

from database import BaseModel


class Step(BaseModel):
    __tablename__ = 'step'

    id = Column(Integer, primary_key=True)
    name_step = Column(String)
