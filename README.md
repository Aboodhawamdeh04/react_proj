# react_proj

# Agriculture Management API

This is a FastAPI backend system for managing agricultural crop data. It provides a RESTful API to retrieve, create, update, and delete crop records, utilizing Pydantic for strict data validation.

## Project Structure
- `models.py`: Contains Pydantic models for data validation.
- `database.py`: Stores the mock dataset.
- `routes.py`: Defines all API endpoints and CRUD operations.
- `main.py`: The application entry point and CORS configuration.

## Setup Instructions

1. **Navigate to the backend directory:**
   ```bash
   cd backend

Create and activate a virtual environment:


python3 -m venv venv
source venv/bin/activate 

Install dependencies:


pip install -r requirements.txt

Run the development server:


uvicorn main:app --reload

