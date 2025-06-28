from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status
import models
from database import engine


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

