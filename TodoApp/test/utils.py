from sqlalchemy import create_engine, text
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from ..database import Base
from fastapi.testclient import TestClient
import pytest
from ..models import Todos, Users
from ..routers.auth import bcrypt_context
from ..main import app


SQLALCHEMY_DATABASE_URL = 'sqlite:///./testdb.db'
engine = create_engine(
    url=SQLALCHEMY_DATABASE_URL, 
    connect_args={'check_same_thread': False}, 
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def override_get_current_user():
    return {'username': 'ycc', 'id': 1, 'user_role': 'admin'}


client = TestClient(app=app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title='Learn to code',
        description='Need to learn everyday',
        priority=5,
        complete=False,
        owner_id=1
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    db.query(Todos).delete()
    db.commit()
    db.close()


@pytest.fixture
def test_user():
    user = Users(
        username='testuser',
        email='testuser@gmail.com',
        first_name='test',
        last_name='user',
        hashed_password=bcrypt_context.hash('testuser_password'),
        role='admin',
        phone_number='0111 111 11 11'
    )

    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user

    db.query(Users).delete()
    db.commit()
    db.close()