from run import *
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import func, create_engine

engine = create_engine("sqlite:///concerts.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def count_user_ids(session):
    return len(session.query(User).all())

def return_band_name_and_total_shows_histogram(session):
    bands = session.query(Band).all()
    band_show_hist = {band.name:len(band.shows) for band in bands}
    return band_show_hist
