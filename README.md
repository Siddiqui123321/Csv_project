# FastAPI CSV Upload and Database Integration

This project demonstrates a FastAPI web application that allows users to upload a CSV file, filter the 'Name' and 'Age' columns, and save the data to an SQLite database.

## Features

- **CSV Upload**: Users can upload a CSV file containing various fields.
- **Database Storage**: The uploaded data is stored in an SQLite database table named 'Users'.
- **Display in Frontend**: The content of the uploaded file is displayed in an HTML table on the frontend.

## Requirements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Jinja2](https://jinja.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

## Installation

1. Install the required dependencies:

    ```bash
    pip install fastapi jinja2 sqlalchemy
    ```

2. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload
    ```

3. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the application.

## Usage

1. Access the application in your browser.
2. Upload a CSV file using the provided form.
3. Click the "Upload" button.
4. Filter the 'Name' and 'Age' columns from the uploaded file.
5. The data will be stored in the 'Users' table in the SQLite database.
6. The uploaded file content will be displayed in an HTML table on the frontend.

## Project Structure

- `main.py`: FastAPI application code.
- `templates/`: Directory containing Jinja2 templates.
  - `upload.html`: HTML template for the file upload form and displayed data.
