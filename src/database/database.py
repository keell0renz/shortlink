from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from .db_schema import Base
import os


def _connect():
    db_string = os.getenv("SHORTLINK_DB_STRING")

    if db_string:
        engine = create_engine(db_string)

    else:
        engine = create_engine(
            "sqlite:///shortlink.db",
            connect_args={
                "check_same_thread": False})

    return engine


def _ensure_schema_exists(session, engine, base, check_for):
    inspector = inspect(session.bind)
    tables = inspector.get_table_names()

    if check_for not in tables:
        base.metadata.create_all(bind=engine)

    session.close()


def _create_get_session(session_class):
    def get_session():
        session = session_class()

        try:
            yield session

        finally:
            session.close()

    return get_session


engine = _connect()

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

_ensure_schema_exists(Session(), engine, Base, "links")

get_session = _create_get_session(Session)
