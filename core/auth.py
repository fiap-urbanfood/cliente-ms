from datetime import datetime, timedelta
from typing import Optional
import httpx
from fastapi import HTTPException, status
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class LoginRequest(BaseModel):
    username: str
    password: str

class AuthService:
    def __init__(self):
        self.login_url = "http://a290354dd0cfd40cbb428316c51cd3ea-2025820054.us-east-1.elb.amazonaws.com:8001/api/v1/usuarios/login"
        self.client = httpx.AsyncClient(timeout=30.0)

    async def authenticate_user(self, username: str, password: str) -> Token:
        try:
            login_data = LoginRequest(username=username, password=password)
            response = await self.client.post(
                self.login_url,
                json=login_data.model_dump(),
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }
            )
            
            if response.status_code == 200:
                return Token(**response.json())
            elif response.status_code == 401:
                error_detail = response.json().get("detail", "Credenciais inválidas")
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=error_detail,
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                error_detail = response.json().get("detail", "Erro ao autenticar")
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"Erro do servidor de autenticação: {error_detail}"
                )
        except httpx.ConnectError:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Serviço de autenticação indisponível"
            )
        except httpx.TimeoutException:
            raise HTTPException(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                detail="Timeout ao conectar com o serviço de autenticação"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro ao autenticar: {str(e)}"
            )
        finally:
            await self.client.aclose()

auth_service = AuthService() 