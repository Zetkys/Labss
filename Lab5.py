class Book:
    def __init__(self, title, author, year):
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError("Название должно быть строкой и не пустым.")
        if not isinstance(author, str) or len(author.strip()) == 0:
            raise ValueError("Автор должен быть строкой и не пустым.")
        if not isinstance(year, int) or year <= 0:
            raise ValueError("Год должен быть положительным числом.")

        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}"

    @classmethod
    def create(cls):
        while True:
            try:
                title = input("Введите название книги: ").strip()
                if not title:
                    raise ValueError("Название книги обязательно!")

                author = input("Введите автора книги: ").strip()
                if not author:
                    raise ValueError("Имя автора обязательно!")

                year = int(input("Введите год издания: "))
                if year <= 0:
                    raise ValueError("Год должен быть положительным числом.")

                return cls(title, author, year)
            except ValueError as e:
                print(e)

    @staticmethod
    def display_books(books_list):
        for idx, book in enumerate(books_list, start=1):
            print(f"{idx}. {book.get_info()}")


class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть больше нуля.")
        self.radius = radius


# Основная программа
saved_books = []

# Добавляем книги
while True:
    new_book = Book.create()
    saved_books.append(new_book)

    continue_adding = input("\nХотите добавить ещё одну книгу? (да/нет): ").lower().strip()
    if continue_adding != 'да':
        break

# Отображаем список книг
print("\nВСЕ СОХРАНЁННЫЕ КНИГИ:")
Book.display_books(saved_books)

# Работа с кругом
try:
    radius = float(input("\nВведите радиус круга: "))
    while radius <= 0:
        print("Ошибка! Радиус должен быть положительным числом.")
        radius = float(input("Попробуйте снова ввести радиус: "))
except ValueError:
    print("Некорректный ввод радиуса.")
else:
    circle = Circle(radius)
    print(f"\nРадиус круга: {circle.radius:.2f}")

    change_answer = input("Изменить радиус? (да/нет): ").lower().strip()
    if change_answer == 'да':
        new_radius = float(input("Введите новый радиус: "))
        while new_radius <= 0:
            print("Ошибка! Новый радиус должен быть положительным числом.")
            new_radius = float(input("Попробуйте снова ввести новый радиус: "))
        circle.radius = new_radius
        print(f"Новый радиус: {circle.radius:.2f}")