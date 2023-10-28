from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.signup import SignupRepository
from sqlalchemy.orm import Session

class DeleteSignupCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)

    async def handle(self, id: int) -> bool:
        result = await self.repo.delete_signup(id)
        return result