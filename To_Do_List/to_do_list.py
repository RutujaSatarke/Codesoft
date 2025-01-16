class ToDoList:
    def __init__(self):
        self.tasks = []

    def add(self):
        task_name = input("Enter your task: ").strip()
        if task_name:
            self.tasks.append({"task": task_name, "completed": False})
            print(f"Task '{task_name}' added successfully!")
        else:
            print("Task name cannot be empty.")

    def view(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{idx}. {task['task']} - {status}")
            print()

    def update(self):
        self.view()
        try:
            task_no = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_no <= len(self.tasks):
                self.tasks[task_no - 1]["completed"] = True
                print(f"Task '{self.tasks[task_no - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def delete(self):
        self.view()
        try:
            task_no = int(input("Enter the task number to delete: "))
            if 1 <= task_no <= len(self.tasks):
                removed_task = self.tasks.pop(task_no - 1)
                print(f"Task '{removed_task['task']}' deleted successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    def menu(self):
        while True:
            print("*"*50)
            print("To-Do List Menu:")
            print("*" * 50)
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Exit")
            print("*" * 50)
            choice = input("Choose an option: ").strip()

            if choice == '1':
                self.add()
            elif choice == '2':
                self.view()
            elif choice == '3':
                self.update()
            elif choice == '4':
                self.delete()
            elif choice == '5':
                print("Exiting To-Do List Application. Bye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the application
app = ToDoList()
app.menu()
