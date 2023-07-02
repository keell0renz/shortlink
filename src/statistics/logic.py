from typing import List, Union
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import and_
from sqlalchemy import or_
from ..database.db_schema import Link, Interactions
from ..exceptions import LinkDoesNotExist

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
    country: Union[str, None]
    user_agent: str

class InteractionsRepository():
    def __init__(self, session: Session):
        self.session = session

    def get_all_link_records(self) -> List[LinkDatabaseRecord]:
        links = self.session.query(Link).all()

        return [LinkDatabaseRecord(**link.__dict__) for link in links]

    def get_all_active_links(self) -> List[LinkDatabaseRecord]:
        active_links = self.session.query(Link).filter(or_(Link.expiration_time == None, Link.expiration_time > datetime.now())).all()

        return [LinkDatabaseRecord(**link.__dict__) for link in active_links]

    def get_all_expired_links(self) -> List[LinkDatabaseRecord]:
        expired_links = self.session.query(Link).filter(and_(Link.expiration_time != None, Link.expiration_time < datetime.now())).all()

        return [LinkDatabaseRecord(**link.__dict__) for link in expired_links]

    def get_link_interactions_by_link_id(self, link_id: str) -> List[InteractionsDatabaseRecord]:
        interactions = self.session.query(Interactions).filter_by(link_id=link_id).all()

        if not interactions:
            if not self.session.query(Link).filter_by(link_id=link_id).first():
                raise LinkDoesNotExist(link_id)

        return [InteractionsDatabaseRecord(**interaction.__dict__) for interaction in interactions]
