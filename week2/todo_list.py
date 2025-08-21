tasks = []
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")
    elif choice == "2":
        if not tasks:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        if not tasks:
            print(" No tasks to mark as done!")
        else:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                done_task = tasks.pop(num-1)
                print(f"Task '{done_task}' completed and removed!")
            else:
                print("Invalid task number!")
    elif choice == "4":
        if not tasks:
            print("No tasks to delete!")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                deleted = tasks.pop(num-1)
                print(f"Task '{deleted}' deleted!")
            else:
                print("Invalid task number!")
    elif choice == "5":
        print("Exiting... Have a productive day!")
        break
    else:
        print("Invalid choice! Please enter 1-5.")

