from typing import Union
from datetime import datetime
from abc import ABC, abstractmethod
from pydantic import BaseModel

from sqlalchemy.orm import Session
from ..database.db_schema import Link, Interactions

class LinkDatabaseRecord(BaseModel):
    link_id: str
    original_link: str
    created_time: datetime
    expiration_time: Union[None, datetime]

class AbstractLinkRepository(ABC):
    @abstractmethod
    def create_link(self, link_id: str, original_link: str) -> None:
        pass

    @abstractmethod
    def get_link_by_link_id(self, link_id: str) -> LinkDatabaseRecord:
        pass

    @abstractmethod
    def delete_link_by_link_id(self, link_id: str) -> None:
        pass

    @abstractmethod
    def change_original_link(self, link_id: str, new_original_link: str) -> None:
        pass

    @abstractmethod
    def change_expiration_time(self, link_id: str, new_expiration_time: datetime) -> None:
        pass

    @abstractmethod
    def add_interaction_by_link(self, link_id: str, ip: str, country: str, user_agent: str) -> None:
        pass

class LinkRepository(AbstractLinkRepository):
    def __init__(self, session: Session):
        self.session = session

    #TODO Repository!

class LinkInterface():
    def __init__(self, repository: AbstractLinkRepository):
        self.repository = repository

    def create_link(self, link_id: str, original_link: str, expiration_time: Union[datetime, None]) -> None:
        self.repository.create_link(link_id, original_link)

        if expiration_time:
            self.repository.change_expiration_time(link_id, expiration_time)

    def get_original_link_by_link_id(self, link_id: str) -> str:
        link_record = self.repository.get_link_by_link_id(link_id)

        return link_record.original_link

    def change_original_link_by_link_id(self, link_id: str, original_link: str) -> None:
        self.repository.change_original_link(link_id, original_link)

    def change_expiration_time_by_link_id(self, link_id: str, expiration_time: Union[datetime, None]) -> None:
        self.repository.change_expiration_time(link_id, expiration_time)

    def delete_link(self, link_id: str) -> None:
        self.repository.delete_link_by_link_id(link_id)
