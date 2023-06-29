from abc import ABC, abstractmethod
from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy import and_
from ..database.db_schema import Link, Interactions

from ..exceptions import LinkAlreadyExists, LinkDoesNotExist, InternalSQLAlchemyError

class LinkDatabaseRecord(BaseModel):
    link_id: str
    original_link: str
    created_time: datetime
    expiration_time: Union[None, datetime]

class InteractionsDatabaseRecord(BaseModel):
    id: int
    link_id: str
    time: datetime
    ip: str
    country: str
    user_agent: str

class AbstractInteractionsRepository(ABC):
    @abstractmethod
    def get_all_link_records(self) -> List[LinkDatabaseRecord]:
        pass

    @abstractmethod
    def get_all_active_links(self) -> List[LinkDatabaseRecord]:
        pass

    @abstractmethod
    def get_all_expired_links(self) -> List[LinkDatabaseRecord]:
        pass

    @abstractmethod
    def get_link_interactions_by_link_id(self, link_id: str) -> List[InteractionsDatabaseRecord]:
        pass

class InteractionsRepository(AbstractInteractionsRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all_link_records(self) -> List[LinkDatabaseRecord]:
        links = self.session.query(Link).all()

        return [LinkDatabaseRecord(**link.__dict__) for link in links]

    def get_all_active_links(self) -> List[LinkDatabaseRecord]:
        active_links = self.session.query(Link).filter(Link.expiration_time > datetime.now()).all()

        return [LinkDatabaseRecord(**link.__dict__) for link in active_links]

    def get_all_expired_links(self) -> List[LinkDatabaseRecord]:
        expired_links = self.session.query(Link).filter(and_(Link.expiration_time != None, Link.expiration_time < datetime.now())).all()

        return [LinkDatabaseRecord(**link.__dict__) for link in expired_links]

    def get_link_interactions_by_link_id(self, link_id: str) -> List[InteractionsDatabaseRecord]:
        link = self.session.query(Link).filter_by(link_id=link_id).first()

        if link is None:
            raise LinkDoesNotExist(link_id)
        
        interactions = self.session.query(Interactions).filter_by(link_id=link_id).all()

        return [InteractionsDatabaseRecord(**interaction.__dict__) for interaction in interactions]
