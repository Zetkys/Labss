import os

def read_file(file_path, mode='full'):

    try:
        if not os.path.exists(file_path):
            return f"Файл '{file_path}' не найден"

        if mode.lower() == 'full':
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        elif mode.lower() == 'line-by-line':
            with open(file_path, 'r') as file:
                lines = [line.strip() for line in file if line.strip()]
                return lines
        else:
            return "Неправильный режим. Используйте 'full' или 'line-by-line'"
    except Exception as e:
        return f"Ошибка при чтении файла: {e}"


def write_file(file_path, text):

    try:
        with open(file_path, 'w') as file:
            file.write(text)
            return f"Текст успешно записан в файл {file_path}."
    except Exception as e:
        return f"Произошла ошибка при записи в файл: {e}"


def append_to_file(file_path, text):

    try:
        with open(file_path, 'a') as file:
            file.write(text + '\n')
            return f"Текст успешно добавлен в файл {file_path}."
    except Exception as e:
        return f"Произошла ошибка при добавлении текста в файл: {e}"


if __name__ == "__main__":
    while True:
        action = input("Что хотите сделать? (читать/записать/дописать/выйти): ").strip().lower()

        if action == 'читать':
            filename = input("Введите название файла для чтения: ")
            method = input("Режим вывода (full / line-by-line): ").strip().lower()

            if method not in ['full', 'line-by-line']:
                print("Неверный режим. Попробуйте снова.")
                continue

            result = read_file(filename, method)
            if isinstance(result, str):
                print(result)
            elif isinstance(result, list):
                for i, line in enumerate(result, start=1):
                    print(f"{i}. {line}")

        elif action == 'записать':
            filename = input("Введите название файла для записи: ")
            new_text = input("Введите текст для записи: ")
            result = write_file(filename, new_text)
            print(result)

        elif action == 'дописать':
            filename = input("Введите название файла для дописки: ")
            new_text = input("Введите текст для дописки: ")
            result = append_to_file(filename, new_text)
            print(result)

        elif action == 'выйти':
            print("Завершение работы")
            break
        else:
            print("Недопустимая команда. Попробуй ещё раз.")