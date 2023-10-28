from typing import Dict, Any
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Signup, Login, Profile_Members, Attendance_Member
from sqlalchemy import desc


class LoginRepository: 
    
    def __init__(self, sess:Session):
        self.sess:Session = sess
    
    async def insert_login(self, login: Login) -> bool: 
        try:
            login = Login(**login)

            self.sess.add(login)
            self.sess.commit()
        except:
            return False
        
        return True
            
    
    async def update_login(self, id:int, details:Dict[str, Any]) -> bool: 
        try:
            self.sess.query(Login).filter(Login.id == id).update(details)     
            self.sess.commit() 
        except: 
            return False 
        
        return True

    async def delete_login(self, id:int) -> bool: 
        try:
            self.sess.query(Login).filter(Login.id == id).delete()
            self.sess.commit()
            
        except: 
            return False 
        return True
    
    async def get_all_login(self):
        return self.sess.query(Login).all() 
    
    async def get_login(self, id:int): 
        return self.sess.query(Login).filter(Login.id == id).one_or_none()