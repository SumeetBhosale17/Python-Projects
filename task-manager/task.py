from datetime import datetime

from colorama import Fore, Style, init
init(autoreset=True)


class Task:
    def __init__(self, title, priority='Medium',
                 completed=False, timestamp=None,
                 due_date=None):
        self._title = title
        self._priority = priority
        self._completed = completed
        self._timestamp = timestamp or datetime.now().isoformat()
        self._due_date = due_date

    @property
    def title(self): return self._title
    @property
    def completed(self): return self._completed
    @completed.setter
    def completed(self, value): self._completed = value
    @property
    def priority(self): return self._priority
    @property
    def timestamp(self): return self._timestamp
    @property
    def due_date(self): return self._due_date

    def to_dict(self):
        return {
            'title': self._title,
            'priority': self._priority,
            'completed': self._completed,
            'timestamp': self._timestamp,
            'due_date': self._due_date
        }

    @staticmethod
    def from_dict(data):
        return Task(**data)

    def __str__(self):
        status = Fore.GREEN + "✔️ Completed" if self.completed else Fore.YELLOW + "❌ Pending"

        if self._priority.lower() == 'high':
            prio_color = Fore.RED
        elif self._priority.lower() == 'medium':
            prio_color = Fore.CYAN
        else:
            prio_color = Fore.BLUE

        return f"{prio_color}{self._title} [{self.priority}] {Fore.MAGENTA} (Due: {self._due_date or 'N/A'}) - {status}{Style.RESET_ALL}"
