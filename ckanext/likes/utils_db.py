from sqlalchemy.ext.declarative import declarative_base


log = __import__('logging').getLogger(__name__)

Base = declarative_base()

def init_tables(engine):
    Base.metadata.create_all(engine)

    