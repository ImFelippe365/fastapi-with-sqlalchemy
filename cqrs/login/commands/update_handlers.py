from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.commands import Command
from sqlalchemy.orm import Session

class UpdateLoginCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)

    async def handle(self, command: Command) -> bool:
        result = await self.repo.update_login(command.details.id, command.details) 
        return result