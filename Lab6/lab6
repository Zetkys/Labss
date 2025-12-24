import hashlib

class UserAccount:
    def __init__(self, username, email, password):
        self._username = username
        self._email = email
        self.__password_hash = hashlib.sha256(password.encode()).hexdigest()

    def _validate_email(self, email):
        if '@' not in email:
            raise ValueError('Адрес электронной почты некорректен.')

    def set_password(self, new_password):
        self.__password_hash = hashlib.sha256(new_password.encode()).hexdigest()
        print("Пароль успешно изменён.")

    def check_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest() == self.__password_hash

    def display_info(self):
        print(f"Имя пользователя: {self._username}\nEmail: {self._email}")


# Регистрация и аутентификация пользователей
print("Создание аккаунта")

username = input("Введите имя пользователя: ")
email = input("Введите email: ")
password = input("Введите пароль: ")

try:
    user = UserAccount(username, email, password)
    print("\nАккаунт успешно создан!\n")
    user.display_info()
except ValueError as err:
    print(err)

# Проверка пароля
print("\nПроверка пароля")
test_password = input("Введите пароль для проверки: ")
if user.check_password(test_password):
    print("Пароль верен!")
else:
    print("Неверный пароль!")

# Изменение пароля
print("\nИзменение пароля")
new_password = input("Введите новый пароль: ")
user.set_password(new_password)

# Повторная проверка пароля
print("\nПроверка нового пароля")
test_new_password = input("Введите новый пароль для проверки: ")
if user.check_password(test_new_password):
    print("Новый пароль подтверждён!")
else:
    print("Пароли не совпадают!")


# Транспортные средства
class Vehicle:
    def __init__(self, make, model):
        if not all([make, model]):
            raise ValueError("Марка и модель обязательны.")
        self.make = make
        self.model = model

    def get_info(self):
        return f"Транспортное средство: {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        valid_fuel_types = {"бензин", "дизель", "электричество", "гибрид"}
        if fuel_type not in valid_fuel_types:
            raise ValueError("Неправильный тип топлива.")
        self.fuel_type = fuel_type

    def get_info(self):
        return f"Автомобиль: {self.make} {self.model}, тип топлива: {self.fuel_type}"



print("\nРабота с транспортными средствами\n")

# Создание базовой машины
make_vehicle = input("Введите марку транспортного средства: ")
model_vehicle = input("Введите модель транспортного средства: ")

try:
    vehicle = Vehicle(make_vehicle, model_vehicle)
    print("Транспорт создано:", vehicle.get_info())
except ValueError as ve:
    print(ve)

# Создание автомобиля
make_car = input("Введите марку автомобиля: ")
model_car = input("Введите модель автомобиля: ")
fuel_type = input("Введите тип топлива (бензин/дизель/электричество/гибрид): ")

try:
    car = Car(make_car, model_car, fuel_type)
    print("Автомобиль создан:", car.get_info())
except ValueError as ve:
    print(ve)

# Полиморфизм
vehicles = [vehicle, car]

# Второй автомобиль
make_car2 = input("Введите марку второго автомобиля: ")
model_car2 = input("Введите модель второго автомобиля: ")
fuel_type2 = input("Введите тип топлива второго автомобиля: ")

try:
    car2 = Car(make_car2, model_car2, fuel_type2)
    vehicles.append(car2)
    print("Второй автомобиль создан:", car2.get_info())
except ValueError as ve:
    print(ve)

# Вывод всех транспортных средств
print("\nВсе созданные транспортные средства:\n")
for i, v in enumerate(vehicles, 1):
    print(f"{i}. {v.get_info()}")
