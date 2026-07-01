from fastapi import APIRouter, status

from app.schemas.task import TaskCreate, TaskResponse
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=list[TaskResponse])
def list_all_tasks() -> list[TaskResponse]:
    """Lista todas as tarefas."""

    return task_service.list_tasks()


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_new_task(task: TaskCreate) -> TaskResponse:
    """Cria uma nova tarefa.

    O FastAPI recebe o JSON, usa o schema TaskCreate para validar os dados e
    só chama esta função quando a entrada está correta.
    """

    return task_service.create_task(task)
