from fastapi import FastAPI
from schemas import Blog

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




@app.get('/')
def index():
    return 'hello'

@app.post('/blog')
def create(request: Blog):
    return request



