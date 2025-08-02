from task import Task
import json
import copy

from colorama import init, Fore
init(autoreset=True)

tasks = []

current_file = "tasks.json"


def get_tasks():
    return tasks


def get_current_file():
    return current_file


def save_tasks():
    with open(current_file, "w") as f:
        json.dump([task.to_dict() for task in tasks], f, indent=4)


def autosave(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        save_tasks()
        return result
    return wrapper


def load_tasks():
    global tasks
    try:
        with open(current_file, 'r') as f:
            tasks = [Task.from_dict(data) for data in json.load(f)]
    except FileNotFoundError:
        tasks = []


@autosave
def add_task(title, priority="Medium", due_date=None):
    push_undo_state()
    tasks.append(Task(title, priority=priority, due_date=due_date))
    print(f"Task {title} added.")


def view_tasks():
    if not tasks:
        print("No tasks yet!")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")


@autosave
def mark_task_completed(index):
    if 0 <= index < len(tasks):
        push_undo_state()
        tasks[index].completed = True
        print(f"Task {tasks[index].title} marked as Completed")
    else:
        print("Invalid Index")


@autosave
def delete_task(index):
    if 0 <= index < len(tasks):
        push_undo_state()
        print(f"Task {tasks[index].title} is Deleted")
        del tasks[index]
    else:
        print("Invalid Index!")


def move_task_up(index):
    if 1 <= index < len(tasks):
        tasks[index - 1], tasks[index] = tasks[index], tasks[index - 1]


def move_task_down(index):
    if 0 <= index < len(tasks) - 1:
        tasks[index + 1], tasks[index] = tasks[index], tasks[index + 1]


def sort_tasks_by_priority():
    tasks.sort(key=lambda t: t.priority)


def search_tasks(keyword):
    return [task for task in tasks if keyword.lower() in task.title.lower()]


@autosave
def clear_completed():
    push_undo_state()
    global tasks
    before = len(tasks)
    tasks = [task for task in tasks if not task.completed]
    after = len(tasks)
    print(f"Cleared {before - after} completed task(s).")
    save_tasks()


def task_summary():
    total = len(tasks)
    completed = len([task for task in tasks if task.completed])
    pending = total - completed
    high_priority = len([task for task in tasks if task.priority.lower() == 'high'])

    print("\n📊 Task Summary")
    print("-" * 20)
    print(Fore.CYAN + f"📝 Total Tasks    : {total}")
    print(Fore.LIGHTGREEN_EX + f"✅ Completed      : {completed}")
    print(Fore.RED + f"⏳ Pending        : {pending}")
    print(Fore.MAGENTA + f"🔥 High Priority  : {high_priority}")


@autosave
def switch_task_list(filename):
    global current_file
    current_file = filename
    load_tasks()
    print(f"Switched to task list: {filename.split('.')[0]}")


MAX_UNDO = 20
undo_stack = []


@autosave
def push_undo_state():
    if len(undo_stack) >= MAX_UNDO:
        undo_stack.pop(0)
    undo_stack.append(copy.deepcopy(tasks))


@autosave
def undo_last_action():
    if undo_stack:
        global tasks
        tasks = undo_stack.pop()
        print("Undid last action!")
    else:
        print("Nothing to undo!")
