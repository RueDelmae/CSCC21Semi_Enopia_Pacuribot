class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def __str__(self):
        status = 'Completed' if self.completed else 'Incomplete'
        return f"{self.name} - {status}"


class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))
        print(f"Task '{name}' added.")

    def view_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

    def filter_tasks(self, completed=True):
        filtered_tasks = [task for task in self.tasks if task.completed == completed]
        if not filtered_tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(filtered_tasks, 1):
                print(f"{i}. {task}")

    def edit_task(self, task_index, new_name):
        if 0 <= task_index < len(self.tasks):
            old_name = self.tasks[task_index].name
            self.tasks[task_index].name = new_name
            print(f"Task '{old_name}' renamed to '{new_name}'.")
        else:
            print("Invalid task number.")

    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f"Task '{self.tasks[task_index].name}' marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task.name}' deleted.")
        else:
            print("Invalid task number. Please input an int")

    def run(self):
        while True:
            print("\n1. Add a Task")
            print("2. View All Tasks")
            print("3. Filter Tasks")
            print("4. Edit a Task")
            print("5. Mark a Task as Complete")
            print("6. Delete a Task")
            print("7. Exit")
            choice = input("Enter choice (1/2/3/4/5/6/7): ")

            if choice == '1':
                name = input("Enter task name: ")
                self.add_task(name)
            elif choice == '2':
                self.view_all_tasks()
            elif choice == '3':
                completed = input("View (C)ompleted or (I)ncomplete tasks? ").lower() == 'c'
                self.filter_tasks(completed)
            elif choice == '4':
                task_index = int(input("Enter task # to edit: ")) - 1
                new_name = input("Enter new task name: ")
                self.edit_task(task_index, new_name)
            elif choice == '5':
                task_index = int(input("Enter task # to mark as complete: ")) - 1
                self.mark_task_complete(task_index)
            elif choice == '6':
                task_index = int(input("Enter task # to delete: ")) - 1
                self.delete_task(task_index)
            elif choice == '7':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    manager = ToDoListManager()
    manager.run()
