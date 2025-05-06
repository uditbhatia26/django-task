from sqlalchemy import Column, Integer, String
from .db import Base

class Member(Base):
    __tablename__ = 'Task1_member'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(200))
    password = Column(String(20))
    file = Column(String(200), nullable=True)  
