from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Profile_Members, Attendance_Member
from datetime import time

class AttendanceRepository():
    def __init__(self, sess: Session):
        self.sess: Session = sess

    async def insert_attendance(self, attendance: Attendance_Member) -> bool:
        attendance['timeout'] = time(attendance['timeout'])
        attendance['timein'] = time(attendance['timein'])

        attendance = Attendance_Member(**attendance)
        self.sess.add(attendance)
        self.sess.commit()

    async def update_attendance(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Attendance_Member).filter(Attendance_Member.id == id).update(details)
            self.sess.commit()
        except:
            return False
        return True

    async def delete_attendance(self, id: int) -> bool:
        try:
            self.sess.query(Attendance_Member).filter(Attendance_Member.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    async def get_all_attendance(self):
        return self.sess.query(Attendance_Member).all()

    async def get_attendance(self, id: int):
        return self.sess.query(Attendance_Member).filter(Attendance_Member.id == id).one_or_none()

    async def join_member_attendance(self):
        return self.sess.query(Profile_Members, Attendance_Member).join(Attendance_Member).all()

    async def outer_join_member(self):
        return self.sess.query(Profile_Members, Attendance_Member).outerjoin(Attendance_Member).all()
