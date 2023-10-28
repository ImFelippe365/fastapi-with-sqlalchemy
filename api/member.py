from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.members import ProfileMembersReq
from typing import List

from cqrs.commands import Command
from cqrs.queries import ListQuery

from cqrs.member.commands.create_handlers import AddMemberCommandHandler
from cqrs.member.commands.update_handlers import UpdateMemberCommandHandler
from cqrs.member.commands.delete_handlers import DeleteMemberCommandHandler
from cqrs.member.query.query_handlers import ListMemberQueryHandler, GetMemberQueryHandler

router = APIRouter(prefix='/members', tags=['Member'])

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def list_all(sess: Session = Depends(sess_db)):
    handler = ListMemberQueryHandler(sess)
    query: ListQuery = await handler.handle()
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.get("/{id}")
async def list_by_id(id: int, sess: Session = Depends(sess_db)):
    handler = GetMemberQueryHandler(sess)
    query: ListQuery = await handler.handle(id)
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.post("/add")
async def create(req: ProfileMembersReq, sess: Session = Depends(sess_db)):
    handler = AddMemberCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo member'}), status_code=500)

@router.put("/update")
async def update(req: ProfileMembersReq, sess: Session = Depends(sess_db)):
    handler = UpdateMemberCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo member'}), status_code=500)

@router.delete("/delete/{id}")
async def delete(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteMemberCommandHandler(sess)

    result = await handler.handle(id)
    if result == True:
        return JSONResponse(content={}, status_code=201)
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo member'}), status_code=500)