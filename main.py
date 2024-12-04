from library import Library

DATA_FILE = "library.json"


def main():
    library = Library(DATA_FILE)

    while True:
        print("\nСистема управления библиотекой:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)
        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.remove_book(book_id)
        elif choice == "3":
            field = input("Введите поле для поиска (title, author, year): ")
            value = input("Введите значение для поиска: ")
            if field == "year":
                value = int(value)
            results = library.search_books(**{field: value})
            for book in results:
                print(
                    f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}")
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            book_id = int(input("Введите ID книги: "))
            status = input("Введите новый статус ('в наличии' или 'выдана'): ")
            library.update_status(book_id, status)
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
