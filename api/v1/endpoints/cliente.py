from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from models.cliente_models import ClienteModel
from schemas.cliente_schemas import ClienteSchema
from core.deps import get_session

router = APIRouter()


# POST CLIENTE
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ClienteSchema)
async def post_curso(cliente: ClienteSchema, db: AsyncSession = Depends(get_session)):  
    novo_cliente = ClienteModel(
        nome=cliente.nome,
        email=cliente.email,
        cpf=cliente.cpf,
        data_aniversario=cliente.data_aniversario,
        profissao=cliente.profissao,
        telefone=cliente.telefone,
        endereco=cliente.endereco
    )
    db.add(novo_cliente)
    await db.commit()
    await db.refresh(novo_cliente)  # Garante que o ID e outros campos sejam atualizados

    return novo_cliente



# GET cursos
@router.get('/', response_model=List[ClienteSchema])
async def get_cursos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ClienteModel)
        result = await session.execute(query)
        cursos: List[ClienteModel] = result.scalars().all()
    return cursos


# GET curso
@router.get("/{curso_id}", response_model=ClienteSchema, status_code=status.HTTP_200_OK)
async def get_curso(cliente_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ClienteModel).filter(ClienteModel.id == cliente_id)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()

        if curso:
            return curso
        else:
            raise HTTPException(
                detail="Curso não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )


# PUT cliente
@router.put(
    "/{curso_id}", response_model=ClienteSchema, status_code=status.HTTP_202_ACCEPTED
)
async def put_curso(
    cliente_id: int, cliente: ClienteSchema, db: AsyncSession = Depends(get_session)
):
    async with db as session:
        query = select(ClienteModel).filter(ClienteModel.id == cliente_id)
        result = await session.execute(query)
        cliente_up = result.scalar_one_or_none()

        if cliente_up:
            cliente_up.nome = cliente.nome
            cliente_up.email = cliente.email
            cliente_up.cpf = cliente.cpf
            cliente_up.data_aniversario = cliente.data_aniversario
            cliente_up.profissao = cliente.profissao
            cliente_up.telefone = cliente.telefone
            cliente_up.endereco = cliente.endereco

            await session.commit()

            return curso_up
        else:
            raise HTTPException(
                detail="Curso não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )


# DELETE cliente
@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_curso(cliente_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ClienteModel).filter(ClienteModel.id == cliente_id)
        result = await session.execute(query)
        curso_del = result.scalar_one_or_none()

        if curso_del:
            await session.delete(curso_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(
                detail="Curso não encontrado.", status_code=status.HTTP_404_NOT_FOUND
            )