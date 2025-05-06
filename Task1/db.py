from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from django.conf import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
