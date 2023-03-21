import typing as t

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from piccolo_admin.endpoints import create_admin
from piccolo_api.crud.serializers import create_pydantic_model
from piccolo_api.fastapi.endpoints import (
    FastAPIWrapper,
    PiccoloCRUD,
    FastAPIKwargs,
)
from piccolo.engine import engine_finder
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from home.endpoints import HomeEndpoint
from home.piccolo_app import APP_CONFIG
from home.tables import Post
from home.tables import Todo
from home.tables import Idea
from piccolo.apps.user.tables import BaseUser

app = FastAPI(
    routes=[
        Route("/", HomeEndpoint),
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes + [BaseUser],
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
        Mount("/static/", StaticFiles(directory="static")),
    ],
)

###############################################################################

###############################################################################


###############################################################################
# Rather than defining the FastAPI endpoints by hand, we can use
# `FastAPIWrapper`, which can save us a lot of time.

FastAPIWrapper(
    "/posts",
    fastapi_app=app,
    piccolo_crud=PiccoloCRUD(Post, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["Post"]},
    ),
)

FastAPIWrapper(
    "/todos",
    fastapi_app=app,
    piccolo_crud=PiccoloCRUD(Todo, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["Todo"]},
    ),
)

FastAPIWrapper(
    "/ideas",
    fastapi_app=app,
    piccolo_crud=PiccoloCRUD(Idea, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["Idea"]},
    ),
)

FastAPIWrapper(
    "/users",
    fastapi_app=app,
    piccolo_crud=PiccoloCRUD(BaseUser, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["BaseUser"]},
    ),
)


###############################################################################


###############################################################################
# Connection pool.

@app.on_event("startup")
async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception:
        print("Unable to connect to the database")


@app.on_event("shutdown")
async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception:
        print("Unable to connect to the database")
