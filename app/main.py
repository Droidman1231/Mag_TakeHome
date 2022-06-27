# External Imports
from fastapi import FastAPI
# User-Defined Imports
from app.api.users import users

app = FastAPI()
app.include_router(users)