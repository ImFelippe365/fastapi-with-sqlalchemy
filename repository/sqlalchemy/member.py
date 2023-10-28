from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Login, Profile_Members, Attendance_Member
from sqlalchemy import desc

class MemberRepository():
    def __init__(self, sess: Session):
        self.sess: Session = sess

    async def insert_member(self, member: Profile_Members) -> bool: 
        member = Profile_Members(**member)
        self.sess.add(member)
        self.sess.commit()
        
    
    async def update_member(self, id: int, details:Dict[str, Any]) -> bool: 
        try:
            self.sess.query(Profile_Members).filter(Profile_Members.id == id).update(details)     
            self.sess.commit() 
        except: 
            return False 
        
        return True

    async def delete_member(self, id:int) -> bool: 
        try:
            self.sess.query(Profile_Members).filter(Profile_Members.id == id).delete()
            self.sess.commit()
        except: 
            return False 
        return True
    
    async def get_all_member(self):
        return self.sess.query(Profile_Members).all() 
    
    async def get_member(self, id:int): 
        return self.sess.query(Profile_Members).filter(Profile_Members.id == id).one_or_none()

    async def join_login_members(self):
        return self.sess.query(Login, Profile_Members).filter(Login.id == Profile_Members.id).all()
