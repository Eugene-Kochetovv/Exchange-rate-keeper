import datetime

from sqlalchemy import Column, Integer, String, Date, Time, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base



Base = declarative_base()

class Currency(Base):
    __tablename__ = "currency"

    abbreviation = Column(String(5), nullable=False, primary_key=True)
    name = Column(String(128), nullable=True)
    rates = relationship("Rates", backref="currency")


class Rates(Base):
    __tablename__ = "rates"

    id = Column(Integer(), autoincrement=True , primary_key=True, index=True)
    currency_abb = Column(String(5), ForeignKey("currency.abbreviation"))
    course = Column(Float(), nullable=False)
    date = Column(Date(), nullable=False)
    time = Column(Time(), nullable=False)
