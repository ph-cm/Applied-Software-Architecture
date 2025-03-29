from fastapi import FastAPI
from routers.alunos import router as router_alunos

app = FastAPI()
app.include_router(router_alunos)