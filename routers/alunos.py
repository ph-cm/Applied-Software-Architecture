from fastapi import APIRouter
from schemas.alunos import Aluno

router = APIRouter(prefix="/api/v1")

@router.get("/alunos")
async def root():
    return {"mensagem": "Dentro de alunos"}

@router.post("/alunos")
async def criar_aluno(aluno: Aluno):
    return {"mensagem": aluno}