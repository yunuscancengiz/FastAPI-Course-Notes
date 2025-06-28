from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(description='ID is not needed on create.', default=None)
    title: str  = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(ge=0, le=5)
    published_date: int = Field(ge=1900, le=2025)

    model_config = {
        'json_schema_extra': {
            'example': {
                'title': 'A new book',
                'author': 'default author',
                'description': 'A new description for book',
                'rating': 5,
                'published_date': 1900
            }
        }
    }


BOOKS = [
    Book(id=1, title='Kızıl Nehiler', author='Jean Christophe Grange', description='detective fiction', rating=4, published_date=2013),
    Book(id=2, title='Sakın Yalan Söyleme', author='Freida McFadden', description='partners in crime', rating=5, published_date=2019),
    Book(id=3, title='Koloni', author='Jean Chritophe Grange', description='not every child is innocent', rating=3, published_date=2007),
    Book(id=4, title='Cehennem', author='Dan Brown', description='so much Dante', rating=4, published_date=2001)
]

app = FastAPI()

@app.get('/books', status_code=status.HTTP_200_OK)
async def read_all_books():
    return BOOKS


@app.get('/books/{book_id}', status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found!')


@app.get('/books/', status_code=status.HTTP_200_OK)
async def read_book_by_rating(rating: int = Query(ge=1, le=5)):
    result = []
    for book in BOOKS:
        if book.rating == rating:
            result.append(book)
    return result


@app.get('/books/publish', status_code=status.HTTP_200_OK)
async def read_books_by_pulished_date(published_date: int = Query(ge=1900, le=2025)):
    result = []
    for i in range(len(BOOKS)):
        if BOOKS[i].published_date == published_date:
            result.append(BOOKS[i])
    return result


@app.post('/create-book', status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(book=new_book))
        

def find_book_id(book: Book):
    book.id = BOOKS[-1].id + 1 if len(BOOKS) > 0 else 1
    return book


@app.put('/books/update_book', status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found!')


@app.delete('/books/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_deleted = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_deleted = True
            break
    if not book_deleted:
        raise HTTPException(status_code=404, detail='Item not found!')


