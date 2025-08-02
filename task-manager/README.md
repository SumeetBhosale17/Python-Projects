<h1 align = "center"> Task Manager </h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Interface-CLI-informational" />
</p>

A simple **Command Line Interface** Task Manager built in Python.
Supports creating, viewing, completing, deleting, reordering, and managing tasks using JSON Files - all via terminal!

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

## Project Structure
task_manager_cli/
├── main.py                  # CLI entry point
├── task.py                  # Core logic: Task Class
├── task_manager.py          # Core logic: TaskManager
├── decorators.py            # Utility decorators
├── utils.py                 # Helper functions
├── tasks.json
└── README.md

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
