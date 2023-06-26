from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func

Base = declarative_base()

class Link(Base):
    __tablename__ = "links"

    link_id = Column(String, unique=True, nullable=False)
    original_link = Column(String, nullable=False)
