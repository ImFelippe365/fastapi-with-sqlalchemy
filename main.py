from fastapi import FastAPI
from api import signup, login, trainer, attendance, member, gym_class

app = FastAPI()
app.include_router(signup.router)
app.include_router(login.router)
app.include_router(trainer.router)
app.include_router(attendance.router)
app.include_router(member.router)
app.include_router(gym_class.router)

