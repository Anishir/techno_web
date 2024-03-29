from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.schemas import Book
import app.services.book as service


app=FastAPI()




@app.post('/books')
def add_new_book(name: str, auteur: str,editeur:str):
    new_book_data = {
        "id": str,
        "name": name,
        "auteur": auteur,
        "editeur":editeur,
    }
    try:
        new_book = Book.model_validate(new_book_data)
    except ValidationError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid name of the book or author or editor for the book.",
        )
    service.save_book(new_book)
    
    return JSONResponse(new_book.model_dump())

    
