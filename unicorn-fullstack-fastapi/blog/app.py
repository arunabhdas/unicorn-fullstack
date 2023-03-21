from starlette.applications import Starlette
from starlette.routing import Mount
from piccolo_admin.endpoints import create_admin
import uvicorn

from home.tables import Post
from home.tables import Todo
from home.tables import Idea

# from schemas import Post

admin = create_admin([Task])
# admin = create_admin([Post])

app = Starlette(routes=[
    Mount('/admin/', admin)
])

if __name__ == "__main__":
    uvicorn.run(app)


