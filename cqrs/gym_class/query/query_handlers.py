from cqrs.handlers import IQueryHandler
from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.queries import ListQuery
from sqlalchemy.orm import Session

class ListGymClassQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self) -> ListQuery:
        data = await self.repo.get_all_gym_class()
        self.query.records = data
        
        return self.query

class GetGymClassQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self, gym_class_id: int) -> ListQuery:
        data = await self.repo.get_gym_class(gym_class_id)
        self.query.records = data
        
        return self.query