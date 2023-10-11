from sqlalchemy import Column, DateTime, ForeignKey, Integer

from database import BaseModel


class BuyStep(BaseModel):
    __tablename__ = 'buy_step'

    id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey('buy.id'))
    step_id = Column(Integer, ForeignKey('step.id'))
    date_step_beg = Column(DateTime)
    date_step_end = Column(DateTime)
