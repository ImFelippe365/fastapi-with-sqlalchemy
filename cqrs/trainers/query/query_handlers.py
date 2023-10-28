from cqrs.handlers import IQueryHandler
from repository.sqlalchemy.trainer import TrainerRepository
from cqrs.queries import ListQuery
from sqlalchemy.orm import Session

class ListTrainerQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self) -> ListQuery:
        data = await self.repo.get_all_trainers()
        self.query.records = data
        
        return self.query

class GetTrainerQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self, trainer_id: int) -> ListQuery:
        data = await self.repo.get_trainer(trainer_id)
        self.query.records = data
        
        return self.query