from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Library Management System")
class Book(BaseModel):
    id: int
    title: str
    author: str
    is_borrowed: bool = False
LIBRARY_DB = [
    {"id": 1, "title": "The Great hermit", "author": "magaso", "is_borrowed": False},
    {"id": 2, "title": "kalunjenje", "author": "elizabeth", "is_borrowed": False},
    {"id": 3, "title": "mabala", "author": "filoteo", "is_borrowed": False},
    {"id": 4, "title": "malingotele", "author": "aurelia", "is_borrowed": False},
    {"id": 5, "title": "history", "author": "kamaleba", "is_borrowed": False}
]
@app.get("/books")
async def get_all_books():
    """List all books in the library"""
    return {"total_books": len(LIBRARY_DB), "books": LIBRARY_DB}
@app.post("/books", status_code=status.HTTP_201_CREATED)
async def add_book(book: Book):
    #Add a new book
    LIBRARY_DB.append(book.dict())
    return {"message": "Book added ", "book": book}
@app.put("/borrow/{book_id}")
async def borrow_book(book_id: int):
    """Mark a book as borrowed"""
    for book in LIBRARY_DB:
        if book["id"] == book_id:
            if book["is_borrowed"]:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, 
                    detail="This book is already out on loan"
                )
            book["is_borrowed"] = True
            return {"message": f"You have borrowed '{book['title']}'"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Book not found in our system"
    )

@app.delete("/remove/{book_id}")
async def remove_book(book_id: int):
    """Remove a book from th"""
    for index, book in enumerate(LIBRARY_DB):
        if book["id"] == book_id:
            LIBRARY_DB.pop(index)
            return {"message": "Book removed from library"}
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Cannot remove: Book ID does not exist"
    )
