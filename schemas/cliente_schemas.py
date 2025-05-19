from typing import Optional

from pydantic import BaseModel as SCBaseModel


class ClienteSchema(SCBaseModel):
    id: Optional[int]
    nome: str
    email: str
    cpf: str
    data_aniversario: str
    profissao: str
    telefone: str
    endereco: str

    class Config:
        orm_mode = True
