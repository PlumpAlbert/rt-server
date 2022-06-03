import app.config as config
from sqlalchemy import create_engine

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, future=True, echo=True)


def get_connection():
    """
    function that returns new connection for a database

    """
    return engine.connect()
