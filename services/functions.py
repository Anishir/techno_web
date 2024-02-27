from app.schemas import Book
from app.database import database



def save_task(add_new_book: Book) -> Book:
    database["books"].append(add_new_book)
    return add_new_book


def afficher_liste_et_nombre_livres() -> list[Book],int:  
    for livre in database["livres"]:
       books_liste= [livre]
        
    total_livres = len(database["livres"])
    print(f"Nombre total de livres : {total_livres}")
    return books_liste, total_livres
