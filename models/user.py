from models.base import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    shows = relationship('Show', secondary='user_shows')


    def total_shows(self):
        return len(self.shows)


    def first_show(self):
        shows = self.shows
        shows.sort(key=lambda shows: shows.date)
        first_show=shows[0]
        return first_show.band.name + ' - ' + first_show.date.strftime('%m/%d/%Y') + ' - ' + first_show.venue.name + ', ' + first_show.venue.city.name
