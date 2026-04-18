def main():
    tasks = []

    while True:
        print("\nSimple Todo App")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task description: ")
            tasks.append({"task": task, "done": False})
            print("Task added.")
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            else:
                for idx, task in enumerate(tasks, start=1):
                    status = "✔" if task["done"] else "✗"
                    print(f"{idx}. [{status}] {task['task']}")
        elif choice == "3":
            if not tasks:
                print("No tasks to complete.")
                continue
            for idx, task in enumerate(tasks, start=1):
                status = "✔" if task["done"] else "✗"
                print(f"{idx}. [{status}] {task['task']}")
            index = input("Enter task number to complete: ")
            if index.isdigit() and 1 <= int(index) <= len(tasks):
                tasks[int(index) - 1]["done"] = True
                print("Task completed.")
            else:
                print("Invalid task number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
