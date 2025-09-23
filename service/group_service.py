from .entity_service import EntityService
from repository.group_repository import GroupRepository

class GroupService(EntityService):
    def __init__(self, repo: GroupRepository = None):
        super().__init__(repo or GroupRepository())
