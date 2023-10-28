from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.login import LoginReq
from typing import List

from cqrs.commands import Command
from cqrs.queries import ListQuery

from cqrs.login.commands.create_handlers import AddLoginCommandHandler
from cqrs.login.commands.update_handlers import UpdateLoginCommandHandler
from cqrs.login.commands.delete_handlers import DeleteLoginCommandHandler
from cqrs.login.query.query_handlers import ListLoginQueryHandler, GetLoginQueryHandler

router = APIRouter(prefix='/login', tags=['Login'])

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def list_all(sess: Session = Depends(sess_db)):
    handler = ListLoginQueryHandler(sess)
    query: ListQuery = await handler.handle()
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.get("/{id}")
async def list_by_id(id: int, sess: Session = Depends(sess_db)):
    handler = GetLoginQueryHandler(sess)
    query: ListQuery = await handler.handle(id)
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.post("/add")
async def create(req: LoginReq, sess: Session = Depends(sess_db)):
    handler = AddLoginCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo login'}), status_code=500)

@router.put("/update")
async def update(req: LoginReq, sess: Session = Depends(sess_db)):
    handler = UpdateLoginCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo login'}), status_code=500)

@router.delete("/delete/{id}")
async def delete(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteLoginCommandHandler(sess)

    result = await handler.handle(id)
    if result == True:
        return JSONResponse(content={}, status_code=201)
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo login'}), status_code=500)
