from typing import Dict


class Book:
    def __init__(self, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = None
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> Dict:
        """Преобразует объект книги в словарь."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: Dict) -> "Book":
        """Создает объект книги из словаря."""
        book = Book(data["title"], data["author"], data["year"], data["status"])
        book.id = data["id"]
        return book
