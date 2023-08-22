from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

_engine = None
_Session = None


def session():
    global _engine, _Session
    if _engine is None:
        from config import the_config
        _engine = create_engine(the_config.DATABASE_URL, echo=the_config.ECHO_SQL)
        _Session = sessionmaker(_engine)
    return _Session()

