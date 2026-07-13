import json
import os
FILE_NAME = "library.json"


def load_library():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except:
        return {}

def save_library(library):
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(library, file, ensure_ascii=False, indent=2)
    except:
        print("Помилка збереження файлу")


def add_book(library):
    print("Назва книги: ", end="")
    title = input()
    print("Автор: ", end="")
    author = input()

    while True:
        try:
            print("Рік видання: ", end="")
            year = int(input())
            break
        except ValueError:
            print("Помилка! Рік видання повинен бути числом.")

    print("Жанр: ", end="")
    genre = input()

    next_id = str(len(library) + 1)

    library[next_id] = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
    }

    save_library(library)
    print("Книгу успішно додано")


def view_all_books(library):
    if not library:
        print("Бібліотека порожня")
        return

    for book_id in library:
        info = library[book_id]
        print(f"ID: {book_id}")
        print(f"Назва: {info['title']}")
        print(f"Автор: {info['author']}")
        print(f"Рік видання: {info['year']}")
        print(f"Жанр: {info['genre']}")
        print()


def delete_book(library):
    print("Введіть ID книги: ", end="")
    book_id = input()

    if book_id in library:
        del library[book_id]
        save_library(library)
    else:
        print("Книгу не знайдено")


def find_books_by_author(library):
    print("Введіть ім'я автора: ", end="")
    search_author = input()

    found = False
    for book_id in library:
        info = library[book_id]
        if info["author"] == search_author:
            print(f"ID: {book_id}")
            print(f"Назва: {info['title']}")
            print(f"Рік видання: {info['year']}")
            print(f"Жанр: {info['genre']}")
            print()
            found = True

    if not found:
        print("Книг цього автора не знайдено")


def main():
    library = load_library()

    while True:
        print("\n- Бібліотека книг ---")
        print("1. Додати книгу")
        print("2. Переглянути всі книги")
        print("3. Видалити книгу")
        print("4. Знайти книгу за автором")
        print("5. Вийти")

        print("Ваш вибір: ", end="")
        choice = input()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            view_all_books(library)
        elif choice == "3":
            delete_book(library)
        elif choice == "4":
            find_books_by_author(library)
        elif choice == "5":
            break
        else:
            print("Неправильний пункт меню")


if __name__ == "__main__":
    main()
