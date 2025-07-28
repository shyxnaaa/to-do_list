import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("No tasks.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{idx}. [{status}] {task['desc']}")

def add_task(tasks):
    desc = input("Enter task description: ").strip()
    if desc:
        tasks.append({"desc": desc, "done": False})
        print("Task added.")
    else:
        print("Empty description. Task not added.")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("Delete task number: "))
        if 1 <= idx <= len(tasks):
            removed = tasks.pop(idx - 1)
            print(f"Deleted: {removed['desc']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def complete_task(tasks):
    list_tasks(tasks)
    try:
        idx = int(input("Complete task number: "))
        if 1 <= idx <= len(tasks):
            tasks[idx - 1]["done"] = True
            print(f"Marked as done: {tasks[idx - 1]['desc']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = load_tasks()
    while True:
        print("\nCommands: list, add, delete, complete, quit")
        cmd = input("Enter command: ").strip().lower()
        if cmd == "list":
            list_tasks(tasks)
        elif cmd == "add":
            add_task(tasks)
            save_tasks(tasks)
        elif cmd == "delete":
            delete_task(tasks)
            save_tasks(tasks)
        elif cmd == "complete":
            complete_task(tasks)
            save_tasks(tasks)
        elif cmd == "quit":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()