from fastapi import FastAPI
from api import admin, login, trainer


app = FastAPI()
app.include_router(admin.router)
app.include_router(login.router)
app.include_router(trainer.router)

