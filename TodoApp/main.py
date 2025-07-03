from fastapi import FastAPI, Request
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

templates = Jinja2Templates(directory='TodoApp/templates')
app.mount('/static', StaticFiles(directory='TodoApp/static'), name='static')


@app.get('/')
def test(request: Request):
    return templates.TemplateResponse('home.html', {'request': request})


@app.get('/healthy')
def health_check():
    return {'status': 'Healthy'}

Base.metadata.create_all(bind=engine)
app.include_router(router=auth.router)
app.include_router(router=todos.router)
app.include_router(router=admin.router)
app.include_router(router=users.router)