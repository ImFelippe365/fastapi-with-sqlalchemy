from cqrs.handlers import IQueryHandler
from repository.sqlalchemy.member import MemberRepository
from cqrs.queries import ListQuery
from sqlalchemy.orm import Session

class ListMemberQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: MemberRepository = MemberRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self) -> ListQuery:
        data = await self.repo.get_all_member()
        self.query.records = data
        
        return self.query

class GetMemberQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: MemberRepository = MemberRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self, member_id: int) -> ListQuery:
        data = await self.repo.get_member(member_id)
        self.query.records = data
        
        return self.query