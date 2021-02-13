from fastapi import APIRouter
from api.v1.actions import employees

routes = APIRouter()

routes.include_router(employees.router, prefix='/employees', tags=['employee'])
