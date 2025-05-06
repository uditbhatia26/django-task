from Task1.db import Base, engine
from Task1.models_sqlalchemy import Member

Base.metadata.create_all(bind=engine)
