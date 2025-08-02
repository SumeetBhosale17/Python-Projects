from datetime import datetime
import json
import os

from colorama import Fore

from task_manager import get_tasks


def get_valid_index(prompt, max_val):
    try:
        index = int(input(prompt)) - 1
        if 0 <= index < max_val:
            return index
    except ValueError:
        pass
    print("Invalid Input..")
    return None


def check_due_tasks():
    today = datetime.today().date()
    due_today = []
    overdue = []

    for task in get_tasks():
        if task.due_date:
            try:
                due_date = datetime.strptime(task.due_date, "%Y-%m-%d").date()
                if due_date == today and not task.completed:
                    due_today.append(task)
                elif due_date < today and not task.completed:
                    overdue.append(task)
            except ValueError:
                print(f"Invalid due date format for task: {task.title}")

    if overdue:
        print("\nOverdue Tasks: ")
        for task in overdue:
            print(f"{Fore.RED}{task.title} (Due: {task.due_date})")

    if due_today:
        print("\nTask Due Today: ")
        for task in due_today:
            print(f"{Fore.RED}{task.title} (Due: {task.due_date})")


def save_backup(tasks):
    backup_file = "backup.bak"

    if os.path.exists(backup_file):
        with open(backup_file, 'r') as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                history = []
    else:
        history = []
    
    history.append([task.to_dict() for task in tasks])

    if len(history) > 20:
        history = history[-20:]
    
    with open(backup_file, 'w') as f:
        json.dump(history, f, indent=4)
