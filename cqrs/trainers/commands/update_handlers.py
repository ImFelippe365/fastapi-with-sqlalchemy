from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.trainer import TrainerRepository
from cqrs.commands import Command
from sqlalchemy.orm import Session

class UpdateTrainerCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)

    async def handle(self, command: Command) -> bool:
        result = await self.repo.update_trainer(command.details)
        return result