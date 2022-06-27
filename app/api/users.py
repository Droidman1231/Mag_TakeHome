from typing import List
from fastapi import Header, APIRouter, HTTPException

from app.api.models import User, Address

user_db = {
            "jdoe" : {
                "username" : "jdoe",
                "name" : "John Doe",
                "address" : {
                    "street1" : "123 example st",
                    "street2" : None,
                    "city" : "nowhere",
                    "state" : "KS",
                    "zip_code" : "12345"
                    }
                }
            }
users = APIRouter()

@users.get('/', response_model = User)
def index():
    return user_db["jdoe"]

@users.post('/', response_model = User)
def lookup_user(username: str):
    if username in user_db.keys():    
        return user_db[username]
    raise HTTPException(status_code = 404, detail = "User with given username was not found")