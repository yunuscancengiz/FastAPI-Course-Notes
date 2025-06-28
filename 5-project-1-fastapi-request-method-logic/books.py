from fastapi import FastAPI, Body

BOOKS = [
    {'title': 'title one', 'author': 'author one', 'category': 'science'},
    {'title': 'title two', 'author': 'author two', 'category': 'science'},
    {'title': 'title three', 'author': 'author three', 'category': 'history'},
    {'title': 'title four', 'author': 'author four', 'category': 'math'},
    {'title': 'title five', 'author': 'author five', 'category': 'math'},
    {'title': 'title six', 'author': 'author two', 'category': 'math'},
]

app = FastAPI()

@app.get('/books')
async def read_all_books():
    return BOOKS


@app.get('/books/{book_title}')
async def read_book(book_title: str):
    for book in BOOKS:
        if book_title.casefold() == book.get('title').casefold():
            return book
    return {'err_msg': f'{book_title} not found!'}


@app.get('/books/')
async def read_category_by_query(category: str):
    result = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            result.append(book)
    return result


@app.get('/books/{author}/')
async def read_author_category_by_query(author: str, category: str):
    result = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold() and book.get('category').casefold() == category.casefold():
            result.append(book)
    return result


@app.post('/books/create_book')
async def create_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put('/books/update_book/')
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete('/books/delete_book/{book_title}')
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break
