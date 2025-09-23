import json
from typing import List, Dict, Optional
from .entity_repository import EntityRepository
from py_utils.logger import plog, DEBUG

USERS_PATH = "exercises/01_basic_concepts/users.json"

class UserRepository(EntityRepository):
    def __init__(self, path: str = USERS_PATH):
        plog("Initializing UserRepository", DEBUG)
        with open(path, "r", encoding="utf-8") as f:
            self.users: List[Dict] = json.load(f)

    def get_all(self) -> List[Dict]:
        plog("UserRepository: get_all", DEBUG)
        return self.users

    def get_by_id(self, id: int) -> Optional[Dict]:
        plog(f"UserRepository: get_by_id({id})", DEBUG)
        return next((u for u in self.users if u.get("id") == id), None)

    def get_by_keyword(self, keyword: str) -> List[Dict]:
        plog(f"UserRepository: get_by_keyword({keyword})", DEBUG)
        if not keyword:
            return []
        kw = keyword.lower()
        return [u for u in self.users if kw in u.get("name","").lower()]
