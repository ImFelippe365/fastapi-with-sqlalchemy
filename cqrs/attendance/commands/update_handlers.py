from cqrs.handlers import ICommandHandler
from repository.sqlalchemy.attendance import AttendanceRepository
from cqrs.commands import Command
from sqlalchemy.orm import Session

class UpdateAttendanceCommandHandler(ICommandHandler):
    
    def __init__(self, sess: Session):
        self.repo: AttendanceRepository = AttendanceRepository(sess)

    async def handle(self, command: Command) -> bool:
        result = await self.repo.update_attendance(command.details.id, command.details)
        return result