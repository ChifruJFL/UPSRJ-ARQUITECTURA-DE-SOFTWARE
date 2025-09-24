# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

from exercises.basic_concepts.repository.interface import UserRepository

class UserService:
    """
    Service component that contains business logic.

    Uses dependency injection to receive a repository instance.
    """

    def __init__(self, repository: UserRepository):
        """Initializes the service with a given repository."""
        plog("Initializing UserService with repository", DEBUG)
        self.repository = repository

    def list_users(self):
        """Retrieves the list of users from the repository."""
        plog("Listing users from service", INFO)
        return self.repository.get_all()
    
    def get_by_keyword(self, keyword: str):
        plog("Retrieving user with keyword", INFO)
        return self.repository.get_by_keyword(keyword=keyword)
    
    def get_by_id(self, id: int):
        plog("Retrieving user with id", INFO)
        return self.repository.get_by_id(id=id)