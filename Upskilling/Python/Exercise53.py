from datetime import datetime

class Task:

    def __init__(
        self,
        name,
        due_date,
        priority
    ):
        self.name = name
        self.due_date = datetime.strptime(
            due_date,
            "%Y-%m-%d"
        )
        self.priority = priority


tasks = [
    Task(
        "Project",
        "2026-01-15",
        1
    ),
    Task(
        "Assignment",
        "2025-12-01",
        2
    )
]

tasks.sort(
    key=lambda x: x.due_date
)

today = datetime.now()

print("Task Schedule")

for task in tasks:

    status = (
        "Overdue"
        if task.due_date < today
        else "Upcoming"
    )

    print(
        task.name,
        task.due_date.date(),
        status
    )

