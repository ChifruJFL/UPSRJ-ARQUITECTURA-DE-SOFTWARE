from .entity_service import EntityService
from repository.user_repository import UserRepository

class UserService(EntityService):
    def __init__(self, repo: UserRepository = None):
        super().__init__(repo or UserRepository())
