from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.commands import Command
from sqlalchemy.orm import Session

class UpdateGymClassCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)

    async def handle(self, command: Command) -> bool:
        result = await self.repo.update_gym_class(command.details.id, command.details)
        return result