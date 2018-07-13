from models.base import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    venues = relationship('Venue', back_populates='city')
