from app.models.task import Task
from app.schemas.task import TaskCreate



_tasks: list[Task] = [
    Task(id=1, title="Preparar workshop", priority=5),
    Task(id=2, title="Estudar Git", priority=3, done=True),
]


def list_tasks() -> list[Task]:
    """Retorna todas as tarefas cadastradas."""

    return _tasks


def create_task(task_data: TaskCreate) -> Task:
    """Cria uma tarefa a partir de dados que já foram validados pelo Pydantic."""

    next_id = max((task.id for task in _tasks), default=0) + 1

    task = Task(
        id=next_id,
        title=task_data.title,
        priority=task_data.priority,
    )
    _tasks.append(task)
    return task
