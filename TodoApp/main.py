from fastapi import FastAPI
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users


app = FastAPI()


@app.get('/healthy')
def health_check():
    return {'status': 'Healthy'}

Base.metadata.create_all(bind=engine)
app.include_router(router=auth.router)
app.include_router(router=todos.router)
app.include_router(router=admin.router)
app.include_router(router=users.router)