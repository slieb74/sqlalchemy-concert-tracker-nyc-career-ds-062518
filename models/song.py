from models.base import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship

class Song(Base):
    __tablename__ = "songs"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    shows = relationship('Show', secondary='show_songs')
