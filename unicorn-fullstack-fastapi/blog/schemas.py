from pydantic import BaseModel

class Post(BaseModel):
    title: str
    body: str

class User(BaseModel):
    name: str
    email: str
    password: str

