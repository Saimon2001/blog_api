from typing import Optional
from pydantic import BaseModel

class Countrie( BaseModel ):
    countrie_id: int
    countrie_name: str