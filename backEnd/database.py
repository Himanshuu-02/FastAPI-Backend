from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url= "postgresql://postgres:Password@localhost:5432/HimanshuDb"
engine= create_engine(db_url)
session= sessionmaker(bind=engine, autoflush=False, autocommit=False)