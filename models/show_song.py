from models.base import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship

class ShowSong(Base):
    __tablename__ = "show_songs"
    id = Column(Integer, primary_key=True)
    length = Column(Integer)
    notes = Column(Text)
    show_id = Column(Integer, ForeignKey('shows.id'))
    song_id = Column(Integer, ForeignKey('songs.id'))
