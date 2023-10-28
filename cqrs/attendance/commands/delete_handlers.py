from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.attendance import AttendanceRepository
from sqlalchemy.orm import Session

class DeleteAttendanceCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: AttendanceRepository = AttendanceRepository(sess)

    async def handle(self, id: int) -> bool:
        result = await self.repo.delete_attendance(id)
        return result