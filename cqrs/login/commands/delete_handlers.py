from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.login import LoginRepository
from sqlalchemy.orm import Session

class DeleteLoginCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)

    async def handle(self, id: int) -> bool:
        result = await self.repo.delete_login(id)
        return result