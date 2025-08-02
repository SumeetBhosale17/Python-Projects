<h1 align = "center"> Task Manager </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Interface-CLI-informational" />
</p>

<p align = "center">
  A simple <b>Command Line Interface</b> Task Manager built in Python.<br/>Supports creating, viewing, completing, deleting, reordering, searching, and managing tasks via JSON file - all from your terminal!
</p>

---

## Features
- ✅ Add, complete, delete tasks
- 📄 Save/load tasks from a `.json` file
- 📆 Set due dates and timestamps
- ⬆️⬇️ Reorder tasks
- 🔍 Search and filter tasks
- 🎯 Multiple task lists (switch between them easily)
- 🎨 Colored terminal output for better UX
- 🧠 Task summaries and priority sorting
- 🔁 Undo support for accidental actions
- 🔧 Auto-save via decorators
- 📦 Argparse-based CLI with flags like `--add`, `--delete`, etc

---

## Project Structure
```
task_manager/
├── main.py                  # CLI entry point
├── task.py                  # Core logic: Task Class
├── task_manager.py          # Core logic: TaskManager
├── decorators.py            # Utility decorators
├── utils.py                 # Helper functions
├── tasks.json
└── README.md
```

---

## How to Use
1. Add a Task
```bash
python main.py --add "Learn ML" --priority "High" --due "2025-08-01"
```

2. View Tasks
```bash
python main.py --view
```

3. Complete a Task
```bash
python main.py complete 1
```

4. Delete a Task
```bash
python main.py delete 1
```

5. Show Summary
```bash
python main.py --summary
```

Help
```bash
python main.py --help
```

---

## CLI Options
| Flag         | Description                    | Example                  |
| ------------ | ------------------------------ | ------------------------ |
| `-tasklist`  | Mention the Task List          | `-tasklist tasks`        |
| `--menu`     | Launch Interactive Menu        | `--menu`                 |
| `--add`      | Add a task                     | `--add "Read book"`      |
| `--priority` | Set priority (High/Medium/Low) | `--priority High`        |
| `--due`      | Set due date (YYYY-MM-DD)      | `--due 2025-08-01`       |
| `--view`     | View all tasks                 | `--view`                 |
| `--summary`  | Show task summary              | `--summary`              |
| `--complete` | Mark a task as completed       | `--complete 2`           |
| `--delete`   | Delete a task                  | `--delete 3`             |
| `--undo`     | Undo Last Action               | `--undo`                 |
| `--search`   | Search tasks by keyword        | `--search ML`            |
| `--clearc`   | Clear completed tasks          | `--clearc`               |
| `--help`     | Show help menu                 | `--help`                 |

---

## 🤝 Contributing
Contributions are welcomed!
- Fork the repo
- Create your feature branch (`git checkout -b feature/YourFeature`)
- Commit your changes (`git commit -m "Add YourFeatures"`)
- Push to the branch (`git push origin feature/YourFeature`)
- Open a Pull Request
