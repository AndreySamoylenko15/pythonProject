from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase



SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:567234@localhost/postgres'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"options": "-csearch_path=hw11"})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass






Base.metadata.create_all(bind=engine)





def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()