import typing as t

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from piccolo_admin.endpoints import create_admin
from starlette.middleware import Middleware
from starlette.routing import Mount, Route

from piccolo_api.openapi.endpoints import swagger_ui
from piccolo_api.token_auth.endpoints import TokenAuthLoginEndpoint
from piccolo_api.session_auth.middleware import SessionsAuthBackend
from piccolo_api.shared.auth.junction import AuthenticationBackendJunction
from starlette.middleware.authentication import AuthenticationMiddleware

from piccolo_api.token_auth.middleware import (
    TokenAuthBackend,
    PiccoloTokenAuthProvider,
)
from piccolo_api.token_auth.tables import TokenAuth

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
from home.tables import Project
from piccolo.apps.user.tables import BaseUser

public_app = FastAPI(
    routes=[
        Route("/", HomeEndpoint),
        Mount(
            "/admin/",
            create_admin(
                tables=APP_CONFIG.table_classes + [BaseUser, TokenAuth],
                # Required when running under HTTPS:
                # allowed_hosts=['my_site.com']
            ),
        ),
        # Session Auth login:
        Route("/login/", TokenAuthLoginEndpoint),
        Mount("/static/", StaticFiles(directory="static")),
    ],
)

###############################################################################
private_app = FastAPI()


protected_app = AuthenticationMiddleware(
    private_app,
    backend=TokenAuthBackend(PiccoloTokenAuthProvider()),
)

FastAPIWrapper(
    "/projects",
    fastapi_app=private_app,
    piccolo_crud=PiccoloCRUD(Project, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["Project"]},
    ),
)

public_app.mount('/private', protected_app)

###############################################################################
FastAPIWrapper(
    "/users",
    fastapi_app=private_app,
    piccolo_crud=PiccoloCRUD(BaseUser, read_only=False),
    fastapi_kwargs=FastAPIKwargs(
        all_routes={"tags": ["BaseUser"]},
    ),
)


###############################################################################


###############################################################################
# Connection pool.

@public_app.on_event("startup")
async def open_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.start_connection_pool()
    except Exception:
        print("Unable to connect to the database")


@public_app.on_event("shutdown")
async def close_database_connection_pool():
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception:
        print("Unable to connect to the database")
