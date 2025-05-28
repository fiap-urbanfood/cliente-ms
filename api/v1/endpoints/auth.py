from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from core.auth import auth_service, Token

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint para autenticação de usuários.
    Recebe username e password e retorna um token JWT.
    """
    token = await auth_service.authenticate_user(form_data.username, form_data.password)
    return token 