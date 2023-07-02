from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Link(Base):
    __tablename__ = "links"

    link_id = Column(String, primary_key=True, unique=True)
    original_link = Column(String, nullable=False)
    created_time = Column(DateTime, default=func.now(), nullable=False)
    expiration_time = Column(DateTime, default=None, nullable=True)
    interactions = relationship("Interactions", backref="link")

class Interactions(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True)
    link_id = Column(String, ForeignKey("links.link_id"), nullable=False)
    time = Column(DateTime, default=func.now(), nullable=False)
    ip = Column(String, nullable=False)
    country = Column(String, nullable=True)
    user_agent = Column(String, nullable=False)