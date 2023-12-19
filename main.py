from fastapi import FastAPI
import models
from routes import router
from config import engine
from typing_extensions import Required, NotRequired


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/students", tags=["students"])

