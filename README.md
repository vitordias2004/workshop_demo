# Workshop Backend — API de Tarefas

Projeto de exemplo para o workshop de **HTTP, FastAPI, Uvicorn, Pydantic, organização de pastas e Git/GitHub**.

## Estrutura

```text
app/
├── main.py                 # Cria a aplicação FastAPI e registra routers
├── routers/
│   └── tasks.py            # Endpoints HTTP
├── schemas/
│   └── task.py             # Schemas Pydantic de entrada e saída
├── services/
│   └── task_service.py     # Regras de negócio
└── models/
    └── task.py             # Modelo interno da tarefa
```

## Criar e ativar o ambiente virtual

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Rodar a API

```bash
uvicorn app.main:app --reload
```

Abra a documentação interativa em:

```text
http://127.0.0.1:8000/docs
```

## Endpoints na versão inicial

| Método | Rota | Descrição | Resposta principal |
|---|---|---|---|
| GET | `/health` | Verifica se a API está no ar | `200 OK` |
| GET | `/tasks` | Lista tarefas | `200 OK` |
| POST | `/tasks` | Cria uma tarefa | `201 Created` |

### Exemplo de `POST /tasks`

```json
{
  "title": "Estudar Pydantic",
  "priority": 2
}
```

### Exemplo de erro de validação

```json
{
  "title": "oi",
  "priority": 9
}
```

Esse payload devolve `422 Unprocessable Entity`, pois o título precisa ter ao menos 3 caracteres e a prioridade deve estar entre 1 e 5.

## Branch para a demo de Git

O repositório já possui uma branch chamada `feat/buscar-tarefa-por-id`. Ela contém a evolução que adiciona `GET /tasks/{task_id}` e permite demonstrar um `404 Not Found`.

```bash
git switch feat/buscar-tarefa-por-id
git log --oneline --all --graph
git diff main...feat/buscar-tarefa-por-id
```

Depois de criar um repositório vazio no GitHub, você pode conectá-lo com:

```bash
git remote add origin URL_DO_SEU_REPOSITORIO
git push -u origin main
git push -u origin feat/buscar-tarefa-por-id
```

> A aplicação usa dados em memória para manter a demo focada nos conceitos.
