from fastapi import FastAPI
from schemas import Blog

app = FastAPI()




@app.get('/')
def index():
    return 'hello'

@app.post('/blog')
def create(request: Blog):
    return request



