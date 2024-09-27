from fastapi import FastAPI
from app.database.configuration import engine
from app.api.models.modelosApp import Usuario
from app.api.routes.rutas import rutas
from starlette.responses import RedirectResponse

#Variable para administrar la aplicacion
app = FastAPI()

#Activo el API
@app.get('/')
def main():
    return RedirectResponse(url = '/docs')

app.include_router(rutas)