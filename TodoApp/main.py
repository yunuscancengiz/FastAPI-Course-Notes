from fastapi import FastAPI, Request, status
from .models import Base
from .database import engine
from .routers import auth, todos, admin, users
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse


app = FastAPI()

app.mount('/static', StaticFiles(directory='TodoApp/static'), name='static')


@app.get('/')
def test(request: Request):
    return RedirectResponse(url='/todos/todo-page', status_code=status.HTTP_302_FOUND)


@app.get('/healthy')
def health_check():
    return {'status': 'Healthy'}

Base.metadata.create_all(bind=engine)
app.include_router(router=auth.router)
app.include_router(router=todos.router)
app.include_router(router=admin.router)
app.include_router(router=users.router)