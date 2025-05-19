from core.configs import settings
from sqlalchemy import Column, Integer, String, Date

class ClienteModel(settings.DBBaseModel):
    __tablename__= 'cliente'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    email    = Column(String(256), nullable=True)
    cpf = Column(String(256), nullable=True)
    data_aniversario = Column(Date, nullable=True)
    profissao = Column(String(256), nullable=True)
    telefone = Column(String(256), nullable=True)
    endereco = Column(String(256), nullable=True)
