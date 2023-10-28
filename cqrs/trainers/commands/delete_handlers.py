from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.trainer import TrainerRepository
from sqlalchemy.orm import Session

class DeleteTrainerCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)

    async def handle(self, id: int) -> bool:
        result = await self.repo.remove_trainer(id)
        return result