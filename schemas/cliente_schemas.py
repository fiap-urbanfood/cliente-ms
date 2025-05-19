from typing import Optional
from datetime import date

from pydantic import BaseModel as SCBaseModel


class ClienteSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    email: str
    cpf: str
    data_aniversario: date
    profissao: str
    telefone: str
    endereco: str

    class Config:
        orm_mode = True
