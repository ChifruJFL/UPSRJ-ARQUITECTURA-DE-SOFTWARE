from typing import List, Dict, Optional
from repository.entity_repository import EntityRepository
from py_utils.logger import plog, DEBUG

class EntityService:
    def __init__(self, repository: EntityRepository):
        plog("Initializing EntityService", DEBUG)
        self.repo = repository

    def get_all(self) -> List[Dict]:
        plog("EntityService: get_all", DEBUG)
        return self.repo.get_all()

    def get_by_id(self, id: int) -> Optional[Dict]:
        plog(f"EntityService: get_by_id({id})", DEBUG)
        return self.repo.get_by_id(id)

    def get_by_keyword(self, keyword: str) -> List[Dict]:
        plog(f"EntityService: get_by_keyword({keyword})", DEBUG)
        return self.repo.get_by_keyword(keyword)
