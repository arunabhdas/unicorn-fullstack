from fastapi import FastAPI, Depends
from schemas import Post

import models, schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.get('/')
def index():
    return 'hello'

@app.post('/blogpost')
def create(request: schemas.Post, db: Session = Depends(get_db)):
    new_post = models.Post(title=request.title, body=request.body)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get('/blogpost')
def get_posts(db: Session = Depends(get_db)):
   posts = db.query(models.Post).all()
   return posts


@app.get('/blogpost/{id}')
def read_post(id, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    return post
