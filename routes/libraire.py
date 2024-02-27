from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from app.schemas import Book
import app.services.book as service


app=FastAPI()



@app.get('/display')
def display_list_of_book_and_number():
    books = service.display_list_of_book_and_number()
    return JSONResponse(
        content={"books": books, "total_books": total_books},  # Retournez les livres avec le nombre total
        status_code=200,
    )


@app.post("/books/update/{id}")
def update_book(id: int , auteur : str , titre : str , editeur : str):
    if id not in data_base :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="book not founded",
        )
    data_base[id] = {"titre" : titre , "auteur" : auteur , "editeur" : editeur }
    print('message ": "book updated successfully')




@app.post("/books/delete/{id}")
def delete_book(id : int):
    if id not in data_base :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="book not found",
        )
    data_base.pop(id)
    print('the book was deleted successfully')




@app.post('/add_book')
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

    
