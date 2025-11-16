# todo.py
# Advanced Console-Based To-Do List with Priority, Completion Status & Colors

from colorama import Fore, Style, init
init(autoreset=True)

TASK_FILE = "elvatelabs\\task.txt"


# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(TASK_FILE, "r") as f:
            for line in f:
                task, priority, status = line.strip().split("|")
                tasks.append({"task": task, "priority": priority, "status": status})
    except FileNotFoundError:
        pass
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        for t in tasks:
            f.write(f"{t['task']}|{t['priority']}|{t['status']}\n")

# Add a new task
def add_task(tasks):
    task = input("Enter a new task: ")
    print("Choose Priority: 1. High  2. Medium  3. Low")
    p = input("Enter priority (1-3): ")

    priority_map = {"1": "High", "2": "Medium", "3": "Low"}
    priority = priority_map.get(p, "Low")

    tasks.append({"task": task, "priority": priority, "status": "Pending"})
    save_tasks(tasks)
    print(Fore.GREEN + "Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print(Fore.RED + "No tasks found.")
        return

    print("\n--- Your To-Do List ---")
    for i, t in enumerate(tasks, 1):
        color = Fore.GREEN if t['status'] == "Completed" else Fore.YELLOW

        print(f"{i}. {color}{t['task']} {Style.RESET_ALL}- "
              f"[Priority: {t['priority']}] - [Status: {t['status']}]")
    print("------------------------\n")

# Mark task as completed
def mark_completed(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    try:
        num = int(input("Enter task number to mark as completed: "))
        tasks[num - 1]['status'] = "Completed"
        save_tasks(tasks)
        print(Fore.GREEN + "Task marked as completed!")
    except:
        print(Fore.RED + "Invalid input!")

# Remove task
def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(Fore.RED + f"Removed: {removed['task']}")
    except:
        print(Fore.RED + "Invalid task number!")

# Search task
def search_task(tasks):
    keyword = input("Enter keyword to search: ").lower()
    results = [t for t in tasks if keyword in t['task'].lower()]

    if not results:
        print(Fore.RED + "No matching tasks found.")
        return

    print("\n--- Search Results ---")
    for t in results:
        print(Fore.CYAN + f"- {t['task']} (Priority: {t['priority']}, Status: {t['status']})")
    print("-----------------------\n")

# Sort tasks by priority
def sort_tasks(tasks):
    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    tasks.sort(key=lambda x: priority_order[x['priority']])
    save_tasks(tasks)
    print(Fore.GREEN + "Tasks sorted by priority!")

# Main Program
def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Search Task")
        print("6. Sort Tasks by Priority")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            search_task(tasks)
        elif choice == "6":
            sort_tasks(tasks)
        elif choice == "7":
            print(Fore.CYAN + "Exiting... Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice! Please try again.")

if __name__ == "__main__":
    main()