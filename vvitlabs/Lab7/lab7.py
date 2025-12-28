class Employee:
    def __init__(self, full_name, staff_number):
        self.full_name = full_name
        self.staff_number = staff_number

    def show_profile(self):
        return f"[EMPLOYEE] {self.full_name} | ID: {self.staff_number}"

    def check_in(self, time_str):
        return f"{self.full_name} вошёл в систему в {time_str}"


class Manager(Employee):
    def __init__(self, full_name, staff_number, unit_name):
        Employee.__init__(self, full_name, staff_number)
        self.unit_name = unit_name

    def assign_deadline(self, project_title, deadline):
        return (f"Проект: «{project_title}» | Дедлайн: {deadline} | "
                f"Ответственный отдел: {self.unit_name} (менеджер: {self.full_name})")

    def show_profile(self):
        base_info = Employee.show_profile(self)
        return f"[MANAGER]  {base_info} | Отдел: {self.unit_name}"


class Technician(Employee):
    def __init__(self, full_name, staff_number, tech_area):
        Employee.__init__(self, full_name, staff_number)
        self.tech_area = tech_area

    def run_diagnostics(self, device_name):
        return (f"Диагностика: устройство «{device_name}» | "
                f"Инженер: {self.full_name} | Область: {self.tech_area}")

    def show_profile(self):
        base_info = Employee.show_profile(self)
        return f"[TECH]     {base_info} | Специализация: {self.tech_area}"


class TechManager(Manager, Technician):
    def __init__(self, full_name, staff_number, unit_name, tech_area):
        Manager.__init__(self, full_name, staff_number, unit_name)
        Technician.__init__(self, full_name, staff_number, tech_area)
        self.subordinates = []

    def include_employee(self, worker):
        if isinstance(worker, Employee):
            self.subordinates.append(worker)
        else:
            raise TypeError("Допускаются только объекты класса Employee и его наследников")

    def describe_team(self):
        if not self.subordinates:
            return f"Команда техменеджера {self.full_name} пока не сформирована."
        lines = [
            "================= КОМАНДА ТЕХМЕНЕДЖЕРА =================",
            f"Руководитель: {self.full_name}",
            "Состав команды:"
        ]
        for idx, member in enumerate(self.subordinates, start=1):
            lines.append(f"  {idx}. {member.show_profile()}")
        lines.append("========================================================")
        return "\n".join(lines)

    def show_profile(self):
        return (f"[TECH-MGR] {self.full_name} | ID: {self.staff_number} | "
                f"Отдел: {self.unit_name} | Зона ответственности: {self.tech_area}")


if __name__ == "__main__":
    base_worker = Employee("Марина Соколова", 101)
    lead_manager = Manager("Дмитрий Орлов", 202, "Разработка ПО")
    field_tech = Technician("Алексей Громов", 303, "Сетевое оборудование")
    chief_tech_manager = TechManager("Кирилл Лебедев", 404, "Инфраструктура", "Серверные системы")

    print("=========== ПРОФИЛИ СОТРУДНИКОВ ===========")
    print(base_worker.show_profile())
    print(lead_manager.show_profile())
    print(field_tech.show_profile())
    print(chief_tech_manager.show_profile())


    print("=========== ДЕЙСТВИЯ СОТРУДНИКОВ ===========")
    print(base_worker.check_in("08:55"))
    print(lead_manager.assign_deadline("Новая платёжная система", "15.02.2026"))
    print(field_tech.run_diagnostics("маршрутизатор R-5500"))
    print(chief_tech_manager.assign_deadline("Обновление дата-центра", "01.06.2026"))
    print(chief_tech_manager.run_diagnostics("кластер хранения данных"))

    chief_tech_manager.include_employee(base_worker)
    chief_tech_manager.include_employee(lead_manager)
    chief_tech_manager.include_employee(field_tech)

    print("=========== СОСТАВ КОМАНДЫ ===========")
    print(chief_tech_manager.describe_team())
