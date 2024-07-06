from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name : str
    email : str
    position : str
    bio : Optional[str]