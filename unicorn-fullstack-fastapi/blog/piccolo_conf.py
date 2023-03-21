from piccolo.engine.postgres import PostgresEngine

from piccolo.conf.apps import AppRegistry
import os
from dotenv import load_dotenv

load_dotenv()

database_host = os.getenv('DATABASE_HOST')
database_name = os.getenv('DATABASE_NAME')
database_username = os.getenv('DATABASE_USERNAME')
database_password = os.getenv('DATABASE_PASSWORD')
database_port= os.getenv('DATABASE_PORT')


DB = PostgresEngine(
    config={
        "database": database_name,
        "user": database_username,
        "password": database_password,
        "host": database_host,
        "port": database_port,
    }
)

#APP_REGISTRY = AppRegistry(
#    apps=["home.piccolo_app", "piccolo_admin.piccolo_app"]
#)

APP_REGISTRY = AppRegistry(
    apps=["piccolo_admin.piccolo_app"]
)
