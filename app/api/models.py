from typing import Dict, Optional
from pydantic import BaseModel, validator

class Address(BaseModel):
    street1: str
    street2: Optional [str]
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    username: str
    name: str
    address: Address #Dict[str,  str] #Address

#@validator('street2')
#def prevent_none(cls, v):
#    assert v is not None, 'street2 may not be None'
#    return v