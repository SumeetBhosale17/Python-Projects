from task_manager import (clear_completed, get_current_file, get_tasks,
                          add_task, load_tasks, move_task_down, move_task_up,
                          save_tasks, search_tasks, switch_task_list,
                          task_summary, undo_last_action,
                          view_tasks, mark_task_completed, delete_task)
from utils import check_due_tasks, get_valid_index

import argparse

from colorama import Fore, Style


def show_menu():
    print(Fore.CYAN +
          f"\n---Task Manager [{get_current_file().split('.')[0]}]---\n"
          + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Add Task")
    print(Fore.BLUE + "2. View Tasks")
    print(Fore.LIGHTGREEN_EX + "3. Mark Task as Completed")
    print(Fore.LIGHTRED_EX + "4. Delete Task")
    print(Fore.LIGHTBLUE_EX + "5. Move Task Up")
    print(Fore.LIGHTBLACK_EX + "6. Move Task Down")
    print(Fore.YELLOW + "7. Search Tasks")
    print(Fore.LIGHTYELLOW_EX + "8. Clear Completed Tasks")
    print(Fore.LIGHTMAGENTA_EX + "9. Tasks Summary")
    print(Fore.BLACK + "10. Switch Task List")
    print(Fore.LIGHTWHITE_EX + "11. Undo Last Action")
    print(Fore.RED + "12. Exit" + Style.RESET_ALL)


def main():
    load_tasks()
    check_due_tasks()

    while True:
        show_menu()
        choice = int(input("\nchoice: "))

        if choice == 1:
            title = input("Enter task title: ")
            priority = input("Enter priority (High/Medium/Low): ")
            add_task(title, priority)
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            view_tasks()
            index = get_valid_index("Enter task number to mark as completed: ",
                                    len(get_tasks()))
            if index is not None:
                mark_task_completed(index)
        elif choice == 4:
            view_tasks()
            index = get_valid_index("Enter task number to delete: ", len(get_tasks()))
            if index is not None:
                delete_task(index)
        elif choice == 5:
            view_tasks()
            index = get_valid_index("Enter task number to move up: ", len(get_tasks()))
            if index is not None:
                move_task_up(index)
        elif choice == 6:
            view_tasks()
            index = get_valid_index("Enter task number to move down: ", len(get_tasks()))
            if index is not None:
                move_task_down(index)
        elif choice == 7:
            keyword = input("Enter keyword to search: ")
            results = search_tasks(keyword)
            if results:
                for i, task in enumerate(results, 1):
                    print(f"{i}. {task}")
            else:
                print("No matching tasks found!")
        elif choice == 8:
            clear_completed()
        elif choice == 9:
            task_summary()
        elif choice == 10:
            save_tasks()
            task_list = input("Enter task list (If list is not present, new list will be created): ").strip().lower() + '.json'
            switch_task_list(task_list)
            check_due_tasks()
        elif choice == 11:
            undo_last_action()
        elif choice == 12:
            save_tasks()
            print("Thank You..!!")
            print("Good Bye..!!")
            break
        else:
            print("Invalid Choice!")


def parse_args():
    parser = argparse.ArgumentParser(description="Task Manager CLI")

    parser.add_argument("--add", type=str, help="Add new task with title")
    parser.add_argument("--priority", type=str, default="Medium", help="Priority of the task")
    parser.add_argument("--due", type=str, help="Due date of the task (YYYY-MM-DD)")

    parser.add_argument("--view", action="store_true", help="View all tasks")
    parser.add_argument("--summary", action="store_true", help="Show task summary")
    parser.add_argument("--complete", type=int, help="Mark a task completed by index")
    parser.add_argument("--delete", type=int, help="Delete a task by index")

    return parser.parse_args()


if __name__ == '__main__':

    load_tasks()
    check_due_tasks()

    args = parse_args()

    if args.add:
        add_task(args.add, args.priority, args.due)
    elif args.view:
        view_tasks()
    elif args.summary:
        task_summary()
    elif args.complete is not None:
        mark_task_completed(args.complete - 1)
    elif args.delete is not None:
        delete_task(args.delete - 1)
    else:
        main()
