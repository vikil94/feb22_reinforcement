class Task:

    due_date = ""
    description = ""

    def __init__(self, description, due_date):
        self.due_date = due_date
        self.description = description


task1 = Task("Do laundry", "On wednesday")
task2 = Task("Take out the garbage", "On Tuesday")
task3 = Task("Go to the gym", "tonight")

print(task1)
print(task2)
print(task3)


class TodoList:

    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        self.task_list.append(task)


my_list = TodoList()
my_list.add_task(task1)
my_list.add_task(task2)
my_list.add_task(task3)

print(my_list)
