import json
# Adjust the import path to include the parent directory for py_utils
import sys
import os
from logging import DEBUG, INFO, WARNING, ERROR
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from py_utils.logger import set_logging, plog

class UserRepository:
    """
    Repository component that handles user data access.

    Implements the Repository design pattern to abstract data retrieval.
    """

    def get_all(self):
        """
        Returns a static list of user dictionaries.

        In a real application, this would query a database.
        """
        plog("Fetching users from repository", DEBUG)
        with open('exercises/basic_concepts/repository/users.json', 'r') as file:
            users = json.load(file)
        return users
    
    def get_by_keyword(self, keyword: str):
        plog(f"Fetching user from repository with keyword {keyword}", DEBUG)
        
        users = self.get_all()
        found = False
        
        keyword = keyword.lower()
        for user in users:
            user_name = user["name"].lower()
            if user_name == keyword:
                found = True
                return user
        if not found:
            return None 
        
    def get_by_id(self, id: int):
        plog(f"Fetching user from repository with id {id}", DEBUG)
        
        users = self.get_all()
        found = False
        
        id = int(id)
        for user in users:
            user_id = int(user["id"])
            if user_id == id:
                found = True
                return user
        if not found:
            return None 