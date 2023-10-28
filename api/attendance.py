from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.attendance import AttendanceMemberReq
from typing import List

from cqrs.commands import Command
from cqrs.queries import ListQuery

from cqrs.attendance.commands.create_handlers import AddAttendanceCommandHandler
from cqrs.attendance.commands.update_handlers import UpdateAttendanceCommandHandler
from cqrs.attendance.commands.delete_handlers import DeleteAttendanceCommandHandler
from cqrs.attendance.query.query_handlers import ListAttendanceQueryHandler, GetAttendanceQueryHandler

router = APIRouter(prefix='/attendance', tags=['Attendance'])

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def list_all(sess: Session = Depends(sess_db)):
    handler = ListAttendanceQueryHandler(sess)
    query: ListQuery = await handler.handle()
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.get("/{id}")
async def list_by_id(id: int, sess: Session = Depends(sess_db)):
    handler = GetAttendanceQueryHandler(sess)
    query: ListQuery = await handler.handle(id)
    
    return JSONResponse(content=jsonable_encoder(query.records), status_code=200)

@router.post("/add")
async def create(req: AttendanceMemberReq, sess: Session = Depends(sess_db)):
    handler = AddAttendanceCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo trainer'}), status_code=500)

@router.put("/update")
async def update(req: AttendanceMemberReq, sess: Session = Depends(sess_db)):
    handler = UpdateAttendanceCommandHandler(sess)
    body = req.dict()

    command = Command()
    command.details = body

    result = await handler.handle(command)
    if result == True:
        return req
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo trainer'}), status_code=500)

@router.delete("/delete/{id}")
async def delete(id: int, sess: Session = Depends(sess_db)):
    handler = DeleteAttendanceCommandHandler(sess)

    result = await handler.handle(id)
    if result == True:
        return JSONResponse(content={}, status_code=201)
    
    return JSONResponse(content=jsonable_encoder({'message: Erro ao tentar criar novo trainer'}), status_code=500)


# @router.get("/members")
# def get_join_member_attendance(sess: Session = Depends(sess_db)):
#     repo: MemberAttendanceRepository = MemberAttendanceRepository(sess)
#     result = repo.join_member_attendance()
#     return result
