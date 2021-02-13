from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

from app.configs import configs

app = FastAPI(
    debug = configs.DEBUG_MODE
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get('/')
def home():
    return {'message': 'Hellow'}

@app.get('/items/{item_id}')
def item_id(item_id: int, q: Optional[str] = None):
    return {'id': item_id, 'q': q}

@app.post('/items/{item_id}')
def add_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}
