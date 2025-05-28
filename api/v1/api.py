from fastapi import APIRouter

from api.v1.endpoints import cliente, auth



api_router = APIRouter()
api_router.include_router(auth.router, prefix='/auth', tags=["auth"])
api_router.include_router(cliente.router, prefix='/cliente', tags=["cliente"])


