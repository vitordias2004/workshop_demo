from fastapi import FastAPI

from app.routers import tasks

app = FastAPI(
    title="Workshop Backend API",
    description="API de tarefas usada na demonstração de FastAPI, Pydantic e Git/GitHub.",
    version="0.1.0",
)

app.include_router(tasks.router)


@app.get("/", include_in_schema=False)
def root() -> dict[str, str]:
    return {"message": "API do workshop está funcionando."}


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Endpoint simples para confirmar que a aplicação está no ar."""

    return {"status": "ok"}
