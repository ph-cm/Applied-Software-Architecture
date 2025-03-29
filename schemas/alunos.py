from pydantic import BaseModel

class Aluno(BaseModel):
    nome: str
    idade: int
    email: str
    curso: str = "Engenharia da Computação"