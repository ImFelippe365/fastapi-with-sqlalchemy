from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.commands import Command
from sqlalchemy.orm import Session

class AddLoginCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)

    async def handle(self, command: Command) -> bool:
        result = await self.repo.insert_login(command.details)
        return result