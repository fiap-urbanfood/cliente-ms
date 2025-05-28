from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from core.auth import TokenData, auth_service

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_session() -> Generator:  # type: ignore
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível validar as credenciais",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Aqui você pode adicionar a lógica para validar o token JWT
        # Por enquanto, vamos apenas retornar o token
        return token
    except JWTError:
        raise credentials_exception