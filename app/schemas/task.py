from pydantic import BaseModel, ConfigDict, Field


class TaskCreate(BaseModel):
    """Dados aceitos quando o cliente cria uma tarefa."""

    title: str = Field(
        min_length=3,
        max_length=80,
        examples=["Estudar FastAPI"],
        description="Título curto e descritivo da tarefa.",
    )
    priority: int = Field(
        default=1,
        ge=1,
        le=5,
        examples=[2],
        description="Prioridade da tarefa: de 1 (baixa) até 5 (alta).",
    )


class TaskResponse(BaseModel):
    """Formato devolvido pela API ao representar uma tarefa."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    priority: int
    done: bool
