from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import json
import os

app = FastAPI()


BOOKS_FILE = "books.json"


class Book(BaseModel):
    id: int
    title: str
    author: str
    genre: Optional[str] = None
    rating: Optional[float] = None


def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            return [Book(**b) for b in json.load(f)]
    return []


def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump([b.dict() for b in books], f, indent=4)


books = load_books()


@app.get("/")
def read_root():
    return {"message": "Book Catalog API is running. Use /docs or Postman to interact."}


@app.get("/books", response_model=List[Book])
def get_books(genre: Optional[str] = None):
    if genre:
        return [book for book in books if book.genre and book.genre.lower() == genre.lower()]
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books", response_model=Book)
def add_book(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(book)
    save_books(books)
    return book


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for i, book in enumerate(books):
        if book.id == book_id:
            del books[i]
            save_books(books)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
