from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import sessionmaker
import csv

app = FastAPI()

# Templates configuration
templates = Jinja2Templates(directory="templates")

# SQLite database setup
engine = create_engine("sqlite:///./test.db")
metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )
metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Model for form data
class Item:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
