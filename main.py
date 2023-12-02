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

# Define a table
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('age', Integer)
              )
# Create the defined table in the SQLite database.
metadata.create_all(engine)

# Set up a session to interact with the database using SQLAlchemy.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Model for form data
class Item:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Function to find column index by name
def find_column_index(headers, column_name):
    try:
        return headers.index(column_name)
    except ValueError:
        return None

# Root endpoint to render the form
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})


# Endpoint to handle file upload and save data to the SQLite database.
@app.post("/")
async def create_upload_file(request: Request, file: UploadFile = File(...)):
    contents = await file.read()
    decoded_content = contents.decode('utf-8').splitlines()
    csv_data = list(csv.reader(decoded_content))

    # Assuming the columns "Name" and "Age" are specified in the template
    name_column_name = "Name"
    age_column_name = "Age"

    # Find column indices dynamically
    headers = csv_data[0]
    name_column_index = find_column_index(headers, name_column_name)
    age_column_index = find_column_index(headers, age_column_name)

    # Check if the specified columns are found in the CSV file.
    if name_column_index is None or age_column_index is None:
        return {"error": "Columns 'Name' and 'Age' not found in the CSV file"}

    # Extract data from columns
    name_column_data = [row[name_column_index] for row in csv_data]
    age_column_data = [row[age_column_index] for row in csv_data]

    # Save data to the SQLite database
    with SessionLocal() as session:
        for name_value, age_value in zip(name_column_data, age_column_data):
            new_user = users.insert().values(name=name_value, age=age_value)
            session.execute(new_user)
        session.commit()

    # data to display in the frontend
    display_data = list(zip(name_column_data, age_column_data))

    # Render the template with the uploaded file content.
    return templates.TemplateResponse("upload.html", {"request": request, "file_content": display_data})