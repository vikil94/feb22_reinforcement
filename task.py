class Task:

    due_date = ""
    description = ""

    def __init__(self, description, due_date):
        self.due_date = due_date
        self.description = description

    def __str__(self):
        return "{} : {}".format(self.description, self.due_date)


class TodoList:
    my_list_of_tasks = []

    def __init__(self):
        self.task_list = []

    @classmethod
    def add_task(cls, description, due_date):
        tasks = Task(description, due_date)
        cls.my_list_of_tasks.append(tasks)


task1 = TodoList.add_task("Do laundry", "On wednesday")
task2 = TodoList.add_task("Take out the garbage", "On Tuesday")
task3 = TodoList.add_task("Go to the gym", "tonight")

print(TodoList.my_list_of_tasks)
