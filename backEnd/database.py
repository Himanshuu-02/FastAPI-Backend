from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()   


#db_url= "postgresql://postgres:Password@localhost:5432/HimanshuDb"
db_url= os.getenv("DATABASE_URL")
print("DB URL LOADED:", db_url)
engine= create_engine(db_url)
session= sessionmaker(bind=engine, autoflush=False, autocommit=False)