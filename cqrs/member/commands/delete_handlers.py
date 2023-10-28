from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.member import MemberRepository
from sqlalchemy.orm import Session

class DeleteMemberCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: MemberRepository = MemberRepository(sess)

    async def handle(self, id: int) -> bool:
        result = await self.repo.delete_member(id)
        return result