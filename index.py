from fastapi import FastAPI
from api.v1 import routes

from app.configs import configs

app = FastAPI(
    debug = configs.DEBUG_MODE
)

app.include_router(routes.routes, prefix='/api/v1')
