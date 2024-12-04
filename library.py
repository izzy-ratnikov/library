import json
import os
from typing import List
from book import Book


class Library:
    def __init__(self, data_file: str):
        self.data_file = data_file
        self.books: List[Book] = self.load_books()

    def load_books(self) -> List[Book]:
        """Загружает книги из файла."""
        if not os.path.exists(self.data_file):
            return []
        with open(self.data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Book.from_dict(book) for book in data]

    def save_books(self):
        """Сохраняет книги в файл."""
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump([book.to_dict() for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title: str, author: str, year: int):
        """Добавляет книгу в библиотеку."""
        book = Book(title, author, year)
        book.id = len(self.books) + 1
        self.books.append(book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {book.id}.")

    def remove_book(self, book_id: int):
        """Удаляет книгу по ID."""
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")

    def find_book_by_id(self, book_id: int) -> Book:
        """Находит книгу по ID."""
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def search_books(self, **kwargs) -> List[Book]:
        """Ищет книги по заданным параметрам."""
        results = self.books
        for key, value in kwargs.items():
            results = [book for book in results if getattr(book, key) == value]
        return results

    def display_books(self):
        """Отображает все книги."""
        if not self.books:
            print("Библиотека пуста.")
            return
        for book in self.books:
            print(
                f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    def update_status(self, book_id: int, status: str):
        """Обновляет статус книги."""
        book = self.find_book_by_id(book_id)
        if book:
            if status in ["в наличии", "выдана"]:
                book.status = status
                self.save_books()
                print(f"Статус книги с ID {book_id} обновлен на '{status}'.")
            else:
                print("Недопустимый статус. Используйте 'в наличии' или 'выдана'.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
