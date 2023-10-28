from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.signup import SignupRepository
from cqrs.commands import ProfileTrainerCommand
from sqlalchemy.orm import Session

class UpdateSignupCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)

    async def handle(self, command: ProfileTrainerCommand) -> bool:
        result = await self.repo.update_signup(command.details.id, command.details)
        return result