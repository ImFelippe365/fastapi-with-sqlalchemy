from cqrs.handlers import IQueryHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.queries import ListQuery
from sqlalchemy.orm import Session

class ListLoginQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self) -> ListQuery:
        data = await self.repo.get_all_login()
        self.query.records = data
        
        return self.query

class GetLoginQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: LoginRepository = LoginRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self, login_id: int) -> ListQuery:
        data = await self.repo.get_login(login_id)
        self.query.records = data
        
        return self.query