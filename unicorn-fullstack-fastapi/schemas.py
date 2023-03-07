from enum import Enum
from typing import Optional
from pydantic import BaseModel

class Error(BaseModel):
    detail: Optional[str] = None

class Priority(Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class CreateTaskSchema(BaseModel):
    priority:Optional[Priority] = 'low'
