from typing import Dict, Any
from sqlalchemy.orm import Session
from domain.data.sqlalchemy_models import Profile_Trainers
from sqlalchemy import desc

class TrainerRepository: 
    
    def __init__(self, sess: Session):
        self.sess:Session = sess
    
    async def insert_trainer(self, trainer: Profile_Trainers) -> bool: 
        try:
            trainer = Profile_Trainers(**trainer)
            
            self.sess.add(trainer)
            self.sess.commit()
        except:
            return False   
        
        return True
    
    async def get_trainer(self, trainer_id: int):
        return self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == trainer_id).one_or_none()
    
    async def get_all_trainers(self):
        return self.sess.query(Profile_Trainers).all()
    
    async def remove_trainer(self, trainer_id: int):
        try:
            self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == trainer_id).delete()
            self.sess.commit()

        except:
            return False
        return True

    async def update_trainer(self, id: int, details: Dict[str, Any]):
        try:
            self.sess.query(Profile_Trainers).filter(Profile_Trainers.id == id).update(details)
            self.sess.commit()

        except:
            return False
        return True