from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI()

# Add CORS middleware to allow React to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:3000", "http://127.0.0.1:5173"], # Add your specific React port here
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods (GET, POST, PUT, DELETE)
    allow_headers=["*"], # Allows all headers
)

@app.get("/")
def home():
    return {"message": "Welcome to the Agriculture Management API"}

# Plug in all the endpoints from routes.py
app.include_router(router)