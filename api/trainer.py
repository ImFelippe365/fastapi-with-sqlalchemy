from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse 
from fastapi.encoders import jsonable_encoder 

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.trainers import ProfileTrainersReq
from domain.data.sqlalchemy_models import Login
from repository.sqlalchemy.login import LoginRepository
from typing import List
from uuid import  uuid4

from cqrs.commands import ProfileTrainerCommand
from cqrs.queries import ProfileTrainerListQuery
from cqrs.trainers.commands.create_handlers import AddTrainerCommandHandler
from cqrs.trainers.commands.update_handlers import UpdateTrainerCommandHandler
from cqrs.trainers.commands.delete_handlers import DeleteTrainerCommandHandler
from cqrs.trainers.query.query_handlers import ListTrainerQueryHandler

router = APIRouter(prefix='/trainers', tags=['Trainers'])

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get_trainers(sess: Session = Depends(sess_db)):
    handler = ListTrainerQueryHandler(sess)
    query:ProfileTrainerListQuery = await handler.handle()
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)
    
@router.post("/add")
async def add_trainer(req: ProfileTrainersReq, sess: Session = Depends(sess_db)):
    handler = AddTrainerCommandHandler(sess)
    mem_profile = dict()
    mem_profile['id'] = 0
    mem_profile['shift'] = req.shift
    mem_profile['age'] = req.age
    mem_profile['firstname'] = req.firstname
    mem_profile['lastname'] = req.lastname
    mem_profile['position'] = req.position
    mem_profile['tenure'] = req.tenure

    command = ProfileTrainerCommand()
    command.details = mem_profile
    result = await handler.handle(command)
    print('RESULTADOOOOO',result)
    if result == True:
        return req
    else:
        return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo trainer'}), status_code=500)