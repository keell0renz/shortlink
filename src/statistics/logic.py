from abc import ABC, abstractmethod
from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

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
