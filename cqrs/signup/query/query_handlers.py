from cqrs.handlers import IQueryHandler
from repository.sqlalchemy.signup import SignupRepository
from cqrs.queries import ListQuery
from sqlalchemy.orm import Session

class ListSignupQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self) -> ListQuery:
        data = await self.repo.get_all_signup()
        self.query.records = data
        
        return self.query

class GetSignupQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: SignupRepository = SignupRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self, signup_id: int) -> ListQuery:
        data = await self.repo.get_signup(signup_id)
        self.query.records = data
        
        return self.query