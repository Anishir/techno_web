from app.schemas import Book
from app.database import database



def save_book(add_new_book: Book) -> Book:
    database["books"].append(add_new_book)
    return add_new_book


def display_list_of_book_and_number() -> list[Book],int:  
    for livre in database["livres"]:
       books_liste= [livre]
        
    total_livres = len(database["livres"])
    print(f"the number of books is : {total_livres}")
    return books_liste, total_livres
