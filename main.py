from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
# Routes
from app.routes import user, auth
# , address, auth
from app.utils import endpoints
###
from starlette.responses import FileResponse
###
import subprocess


# APP CONFIG
app = FastAPI(
    title="APP-ONE-NoSQL-API",
    version="1.0.5",
    contact={
        "name": "Nícolas Marques de Moura Barbosa",
        "url": "https://www.linkedin.com/in/nicolasmmb/",
        "email": "nicolas.mmb@hotmail.com",
    },

)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES
app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/api")
app.include_router(endpoints.router, prefix="/api")


# ROUTE
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    path = './app/configs/favicon/favicon.png'
    return FileResponse(path)


@app.get('/', include_in_schema=False)
def index():
    return RedirectResponse("/docs")
