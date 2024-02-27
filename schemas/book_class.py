from pydantic import BaseModel, Field


class Book(BaseModel):
    id: int
    name_book: str = Field(...,min_length=1,strip_whitespace=True)
    auteur:str=Field(...,min_length=1,strip_whitespace=True)
    editeur:str =Field(...,min_length=1,strip_whitespace=True)
