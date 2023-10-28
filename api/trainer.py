from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse 
from fastapi.encoders import jsonable_encoder 

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.trainers import ProfileTrainersReq

from cqrs.commands import Command
from cqrs.queries import ListQuery

from cqrs.trainers.commands.create_handlers import AddTrainerCommandHandler
from cqrs.trainers.commands.update_handlers import UpdateTrainerCommandHandler
from cqrs.trainers.commands.delete_handlers import DeleteTrainerCommandHandler
from cqrs.trainers.query.query_handlers import ListTrainerQueryHandler, GetTrainerQueryHandler

router = APIRouter(prefix='/trainers', tags=['Trainers'])

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def list_all(sess: Session = Depends(sess_db)):
    handler = ListTrainerQueryHandler(sess)
    query: ListQuery = await handler.handle()
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.get("/{id}")
async def list_by_id(id: int, sess: Session = Depends(sess_db)):
    handler = GetTrainerQueryHandler(sess)
    query: ListQuery = await handler.handle(id)
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.post("/add")
async def create(req: ProfileTrainersReq, sess: Session = Depends(sess_db)):
    handler = AddTrainerCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo trainer'}), status_code=500)

@router.put("/update")
async def update(req: ProfileTrainersReq, sess: Session = Depends(sess_db)):
    handler = UpdateTrainerCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar atualizar'}), status_code=500)

@router.delete("/delete/{id}")
async def delete(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteTrainerCommandHandler(sess)

    result = await handler.handle(id)
    if result == True:
        return JSONResponse(content={}, status_code=201)
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar remover trainer'}), status_code=500)