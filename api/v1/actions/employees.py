from fastapi import APIRouter
from models.employee import Add

router = APIRouter()

@router.post('/add')
def add_employee(data: Add):
    return data
