from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry
import os

database_host = os.environ.get('DATABASE_HOST', '')
database_name = os.environ.get('DATABASE_NAME', '')
database_username = os.environ.get('DATABASE_USERNAME', '')
database_password = os.environ.get('DATABASE_PASSWORD', '')
database_port= os.environ.get('DATABASE_PORT', '')


DB = PostgresEngine(
    config={
        "database": database_name,
        "user": database_username,
        "password": database_password,
        "host": database_host,
        "port": database_port,
    }
)

APP_REGISTRY = AppRegistry(
    apps=["home.piccolo_app", "piccolo_admin.piccolo_app"]
)
