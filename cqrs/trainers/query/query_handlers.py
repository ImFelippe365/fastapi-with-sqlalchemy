from cqrs.handlers import IQueryHandler
from repository.sqlalchemy.trainer import TrainerRepository
from cqrs.commands import ProfileTrainerCommand
from cqrs.queries import ProfileTrainerListQuery
from sqlalchemy.orm import Session

class ListTrainerQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)
        self.query: ProfileTrainerListQuery = ProfileTrainerListQuery()

    async def handle(self) -> ProfileTrainerListQuery:
        data = await self.repo.get_all_member()
        self.query.records = data
        
        return self.query