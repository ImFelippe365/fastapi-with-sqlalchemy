from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.members import GymClassReq
from typing import List

from cqrs.commands import Command
from cqrs.queries import ListQuery

from cqrs.gym_class.commands.create_handlers import AddGymClassCommandHandler
from cqrs.gym_class.commands.update_handlers import UpdateGymClassCommandHandler
from cqrs.gym_class.commands.delete_handlers import DeleteGymClassCommandHandler
from cqrs.gym_class.query.query_handlers import ListGymClassQueryHandler, GetGymClassQueryHandler

router = APIRouter(prefix='/gym-class', tags=['GymClass'])

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def list_all(sess: Session = Depends(sess_db)):
    handler = ListGymClassQueryHandler(sess)
    query: ListQuery = await handler.handle()
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.get("/{id}")
async def list_by_id(id: int, sess: Session = Depends(sess_db)):
    handler = GetGymClassQueryHandler(sess)
    query: ListQuery = await handler.handle(id)
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.post("/add")
async def create(req: GymClassReq, sess: Session = Depends(sess_db)):
    handler = AddGymClassCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo gymclass'}), status_code=500)

@router.put("/update")
async def update(req: GymClassReq, sess: Session = Depends(sess_db)):
    handler = UpdateGymClassCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar atualizar gymclass'}), status_code=500)

@router.delete("/delete/{id}")
async def delete(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteGymClassCommandHandler(sess)

    result = await handler.handle(id)
    if result == True:
        return JSONResponse(content={}, status_code=201)
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo trainer'}), status_code=500)