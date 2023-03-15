from enum import Enum
from typing import Optional
from pydantic import BaseModel

class Error(BaseModel):
    detail: Optional[str] = None

class Priority(Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'

class Status(Enum):
    progress = 'progress'
    pending = 'pending'
    completed = 'completed'

class CreateTaskSchema(BaseModel):
    priority:Optional[Priority] = 'low'
    status: Optional[Status] = 'pending'
