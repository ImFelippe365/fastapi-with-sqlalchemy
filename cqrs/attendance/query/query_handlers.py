from cqrs.handlers import IQueryHandler
from repository.sqlalchemy.attendance import AttendanceRepository
from cqrs.queries import ListQuery
from sqlalchemy.orm import Session

class ListAttendanceQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: AttendanceRepository = AttendanceRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self) -> ListQuery:
        data = await self.repo.get_all_attendance()
        self.query.records = data
        
        return self.query

class GetAttendanceQueryHandler(IQueryHandler):
    
    def __init__(self, sess: Session):
        self.repo: AttendanceRepository = AttendanceRepository(sess)
        self.query: ListQuery = ListQuery()

    async def handle(self, attendance_id: int) -> ListQuery:
        data = await self.repo.get_attendance(attendance_id)
        self.query.records = data
        
        return self.query