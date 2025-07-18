# Необходимо создать класс, который позволяет управлять задачами.
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Необходимо реализовать функцию для добавления задач, отметки выполненных задач и
# вывода списка текущих(невыполненных) задач.

class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False  # По умолчанию задача не выполнена

    def mark_completed(self):
        self.completed = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def complete_task(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                break

    def show_current_tasks(self):
        for task in self.tasks:
            if task.completed == False:  # Явное использование False
                print(f"- {task.description} (Срок: {task.deadline})")


# Пример использования:
manager = TaskManager()

manager.add_task("Написать отчет", "20.07.2025")
manager.add_task("Позвонить клиенту", "18.07.2025")

manager.complete_task("Позвонить клиенту")

print("Текущие задачи:")
manager.show_current_tasks()



