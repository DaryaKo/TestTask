from fastapi import APIRouter

from server.api_v1.endpoints import employees

server_api_router = APIRouter()
server_api_router.include_router(employees.server_router, prefix='/employees', tags=['employees'])
