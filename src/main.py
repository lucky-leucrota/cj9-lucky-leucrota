from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.requests import Request

from .routers import chat

# App Config
app = FastAPI(
    title="Dis-Code",
    version="Dev.3.8.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")
app.include_router(chat.router)

# Exception Handlers and etc...
@app.exception_handler(404)
async def Custom_404_handler(request: Request, __):
    """Custom 404 handler"""
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
