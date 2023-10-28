from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.member import MemberRepository
from cqrs.commands import Command
from sqlalchemy.orm import Session

class AddMemberCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: MemberRepository = MemberRepository(sess)

    async def handle(self, command: Command) -> bool:
        result = await self.repo.insert_member(command.details)
        return result