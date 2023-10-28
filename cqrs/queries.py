from typing import List, Any
from domain.data.sqlalchemy_models import Profile_Trainers,Login

class ListQuery:

    def __init__(self):
        self._records: List[Any, None] = list()

    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records