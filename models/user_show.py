from models.base import Base
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, relationship

class UserShow(Base):
    __tablename__ = "user_shows"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    show_id = Column(Integer, ForeignKey('shows.id'))
