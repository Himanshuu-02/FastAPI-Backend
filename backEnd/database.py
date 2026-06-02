from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()   


#db_url= "postgresql://postgres:Password@localhost:5432/HimanshuDb"
db_url= os.getenv("DATABASE_URL")
print("DB URL LOADED:", db_url)
import logging
# enable basic SQLAlchemy engine logging (INFO shows executed statements)
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine= create_engine(
	db_url,
	pool_pre_ping=True,
	pool_size=10,
	max_overflow=20,
	echo=False,
)

session= sessionmaker(bind=engine, autoflush=False, autocommit=False)