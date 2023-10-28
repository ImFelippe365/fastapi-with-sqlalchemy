from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.trainer import TrainerRepository
from cqrs.commands import ProfileTrainerCommand
from sqlalchemy.orm import Session

class AddTrainerCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)

    async def handle(self, command: ProfileTrainerCommand) -> bool:
        result = await self.repo.insert_trainer(command.details)
        return result