from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from db_config.sqlalchemy_connect import SessionFactory
from domain.request.signup import SignupReq
from domain.data.sqlalchemy_models import Signup
from repository.sqlalchemy.signup import SignupRepository
from typing import List

router = APIRouter(prefix='/signup', tags=['Signup'])


def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

@router.post("/add")
def add_signup(req: SignupReq, sess: Session = Depends(sess_db)):
    repo: SignupRepository = SignupRepository(sess)
    signup = Signup(password=req.password, username=req.username, id=req.id)
    result = repo.insert_signup(signup)
    if result == True:
        return signup
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'}, status_code=500)


@router.get("/list", response_model=List[SignupReq])
def list_signup(sess: Session = Depends(sess_db)):
    repo: SignupRepository = SignupRepository(sess)
    result = repo.get_all_signup()
    return result


@router.patch("/update")
def update_signup(id: int, req: SignupReq, sess: Session = Depends(sess_db)):
    signup_dict = req.dict(exclude_unset=True)
    repo: SignupRepository = SignupRepository(sess)
    result = repo.update_signup(id, signup_dict)
    if result:
        return JSONResponse(content={'message': 'profile updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update profile error'}, status_code=500)


@router.delete("/delete/{id}")
def delete_signup(id: int, sess: Session = Depends(sess_db)):
    repo: SignupRepository = SignupRepository(sess)
    result = repo.delete_signup(id)
    if result:
        return JSONResponse(content={'message': 'profile deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete profile error'}, status_code=500)


@router.get("/list/{id}", response_model=SignupReq)
def get_signup(id: int, sess: Session = Depends(sess_db)):
    repo: SignupRepository = SignupRepository(sess)
    result = repo.get_signup(id)
    return result




