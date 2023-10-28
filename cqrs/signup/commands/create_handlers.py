from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.signup import SignupRepository
from cqrs.commands import Command
from sqlalchemy.orm import Session

class AddSignupCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)

    async def handle(self, command: Command) -> bool:
        result = await self.repo.insert_signup(command.details)
        return result