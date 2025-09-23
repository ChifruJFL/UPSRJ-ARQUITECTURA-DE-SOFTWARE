from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class EntityRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Dict]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[Dict]:
        pass

    @abstractmethod
    def get_by_keyword(self, keyword: str) -> List[Dict]:
        pass
