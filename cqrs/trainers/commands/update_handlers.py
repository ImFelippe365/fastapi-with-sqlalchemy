from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.trainer import TrainerRepository
from cqrs.commands import ProfileTrainerCommand
from sqlalchemy.orm import Session

class UpdateTrainerCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: TrainerRepository = TrainerRepository(sess)

    async def handle(self, command: ProfileTrainerCommand) -> bool:
        result = await self.repo.update_member(command.details)
        return result