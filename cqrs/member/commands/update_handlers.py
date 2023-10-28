from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.member import MemberRepository
from cqrs.commands import Command
from sqlalchemy.orm import Session

class UpdateMemberCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: MemberRepository = MemberRepository(sess)

    async def handle(self, command: Command) -> bool:
        result = await self.repo.update_member(command.details.id, command.details)
        return result