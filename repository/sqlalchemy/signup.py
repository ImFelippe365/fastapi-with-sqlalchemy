from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Signup, Login, Profile_Members, Attendance_Member
from sqlalchemy import desc


class SignupRepository:

    def __init__(self, sess: Session):
        self.sess: Session = sess

    async def insert_signup(self, signup: Signup) -> bool:
        try:
            signup = Signup(**signup)
            self.sess.add(signup)
            self.sess.commit()
        except:
            return False
        return True

    async def update_signup(self, id: int, details: Dict[str, Any]) -> bool:
        try:
            self.sess.query(Signup).filter(Signup.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True

    async def delete_signup(self, id: int) -> bool:
        try:
            signup = self.sess.query(Signup).filter(Signup.id == id).delete()
            self.sess.commit()

        except:
            return False
        return True

    async def get_all_signup(self):
        return self.sess.query(Signup).all()

    async def get_all_signup_where(self, username: str):
        return self.sess.query(Signup.username, Signup.password).filter(Signup.username == username).all()

    async def get_all_signup_sorted_desc(self):
        return self.sess.query(Signup.username, Signup.password).order_by(desc(Signup.username)).all()

    async def get_signup(self, id: int):
        return self.sess.query(Signup).filter(Signup.id == id).one_or_none()




