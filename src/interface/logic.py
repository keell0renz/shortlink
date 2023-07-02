from typing import Union
import datetime
from pydantic import BaseModel

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from ..database.db_schema import Link, Interactions

from ..exceptions import LinkAlreadyExists, LinkDoesNotExist, LinkHasExpired, InternalSQLAlchemyError

class LinkDatabaseRecord(BaseModel):
    link_id: str
    original_link: str
    created_time: datetime.datetime
    expiration_time: Union[None, datetime.datetime]

class LinkRepository():
    def __init__(self, session: Session):
        self.session = session

    def create_link(self, link_id: str, original_link: str) -> None:
        try:
            link = Link(link_id=link_id, original_link=original_link)
            self.session.add(link)
            self.session.commit()

        except IntegrityError:
            self.session.rollback()
            raise LinkAlreadyExists(link_id)
        
        except SQLAlchemyError as e:
            self.session.rollback()
            raise InternalSQLAlchemyError(str(e))

    def get_link_by_link_id(self, link_id: str) -> LinkDatabaseRecord:
        link = self.session.query(Link).filter_by(link_id=link_id).first()

        if link is None:
            raise LinkDoesNotExist(link_id)
        
        return LinkDatabaseRecord(**link.__dict__)

    def delete_link_by_link_id(self, link_id: str) -> None:
        try:
            link = self.session.query(Link).filter_by(link_id=link_id).first()
            if link is None:
                raise LinkDoesNotExist(link_id)
            
            self.session.delete(link)
            self.session.commit()

        except SQLAlchemyError as e:
            self.session.rollback()
            raise InternalSQLAlchemyError(str(e))

    def change_original_link(self, link_id: str, new_original_link: str) -> None:
        try:
            link = self.session.query(Link).filter_by(link_id=link_id).first()
            if link is None:
                raise LinkDoesNotExist(link_id)
            
            link.original_link = new_original_link
            self.session.commit()

        except IntegrityError:
            self.session.rollback()
            raise LinkAlreadyExists(link_id)
        
        except SQLAlchemyError as e:
            self.session.rollback()
            raise InternalSQLAlchemyError(str(e))

    def change_expiration_time(self, link_id: str, new_expiration_time: datetime) -> None:
        try:
            link = self.session.query(Link).filter_by(link_id=link_id).first()
            if link is None:
                raise LinkDoesNotExist(link_id)
            
            link.expiration_time = new_expiration_time
            self.session.commit()

        except SQLAlchemyError as e:
            self.session.rollback()
            raise InternalSQLAlchemyError(str(e))

    def add_interaction_by_link(self, link_id: str, ip: str, country: str, user_agent: str) -> None:
        try:
            link = self.session.query(Link).filter_by(link_id=link_id).first()
            if link is None:
                raise LinkDoesNotExist(link_id)
            
            interaction = Interactions(link_id=link_id, ip=ip, country=country, user_agent=user_agent)
            self.session.add(interaction)
            self.session.commit()
            
        except SQLAlchemyError as e:
            self.session.rollback()
            raise InternalSQLAlchemyError(str(e))


class LinkInterface():
    def __init__(self, repository: LinkRepository):
        self.repository = repository

    def create_link(self, link_id: str, original_link: str, expiration_time: Union[str, None]) -> None:
        self.repository.create_link(link_id, original_link)

        if expiration_time:
            expiration_time = datetime.datetime.strptime(expiration_time, "%d/%m/%Y-%H:%M:%S")

            self.repository.change_expiration_time(link_id, expiration_time)

    def get_link_data(self, link_id: str) -> dict:
        link_record = self.repository.get_link_by_link_id(link_id)

        if link_record.expiration_time != None:
            expiration_time = link_record.expiration_time.strftime("%d/%m/%Y-%H:%M:%S")

        else:
            expiration_time = "None"

        return {
            "link_id": link_record.link_id,
            "original_link": link_record.original_link,
            "created_time": link_record.created_time.strftime("%d/%m/%Y-%H:%M:%S"),
            "expiration_time": expiration_time
        }

    def get_original_link_by_link_id(self, link_id: str) -> str:
        link_record = self.repository.get_link_by_link_id(link_id)

        if link_record.expiration_time != None:
            if link_record.expiration_time <= datetime.datetime.now():
                raise LinkHasExpired(link_id)

        return link_record.original_link

    def change_original_link_by_link_id(self, link_id: str, original_link: str) -> None:
        self.repository.change_original_link(link_id, original_link)

    def change_expiration_time_by_link_id(self, link_id: str, expiration_time: Union[str, None]) -> None:
        if expiration_time == None:
            self.repository.change_expiration_time(link_id, None)

        else:
            expiration_time = datetime.datetime.strptime(expiration_time, "%d/%m/%Y-%H:%M:%S")
        
            self.repository.change_expiration_time(link_id, expiration_time)

    def delete_link(self, link_id: str) -> None:
        self.repository.delete_link_by_link_id(link_id)

    def add_interaction(self, link_id: str, ip: str, country: str, user_agent: str) -> None:
        self.repository.add_interaction_by_link(link_id, ip, country, user_agent)
