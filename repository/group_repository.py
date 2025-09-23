import json
from typing import List, Dict, Optional
from .entity_repository import EntityRepository
from py_utils.logger import plog, DEBUG

GROUPS_PATH = "exercises/01_basic_concepts/groups.json"
USERS_PATH = "exercises/01_basic_concepts/users.json"

class GroupRepository(EntityRepository):
    def __init__(self, path: str = GROUPS_PATH, users_path: str = USERS_PATH):
        plog("Initializing GroupRepository", DEBUG)
        with open(path, "r", encoding="utf-8") as f:
            self.groups: List[Dict] = json.load(f)
        with open(users_path, "r", encoding="utf-8") as f:
            self.users: List[Dict] = json.load(f)

    def get_all(self) -> List[Dict]:
        plog("GroupRepository: get_all", DEBUG)
        return self.groups

    def get_by_id(self, id: int) -> Optional[Dict]:
        plog(f"GroupRepository: get_by_id({id})", DEBUG)
        grp = next((g for g in self.groups if g.get("id") == id), None)
        if grp:
            # expandir miembros con info de usuario
            grp_copy = dict(grp)
            grp_copy["members_info"] = [u for u in self.users if u["id"] in grp_copy.get("members",[])]
            return grp_copy
        return None

    def get_by_keyword(self, keyword: str) -> List[Dict]:
        plog(f"GroupRepository: get_by_keyword({keyword})", DEBUG)
        if not keyword:
            return []
        kw = keyword.lower()
        res = [g for g in self.groups if kw in g.get("name","").lower()]
        # expandir members_info para cada resultado
        for g in res:
            g["members_info"] = [u for u in self.users if u["id"] in g.get("members",[])]
        return res
