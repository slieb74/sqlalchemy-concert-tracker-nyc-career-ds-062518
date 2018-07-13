from models.base import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship

class Band(Base):
    __tablename__ = "bands"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    shows = relationship('Show', back_populates='band')
