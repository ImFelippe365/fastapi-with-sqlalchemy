from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.gym_class import GymClassRepository
from sqlalchemy.orm import Session

class DeleteGymClassCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: GymClassRepository = GymClassRepository(sess)

    async def handle(self, id: int) -> bool:
        result = await self.repo.delete_gym_class(id)
        return result