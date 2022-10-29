from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routes import chat

templates = Jinja2Templates(directory="src/templates")

app = FastAPI(version="Prod.1.0.0", docs_url=None, redoc_url=None, openapi_url=None)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(chat.router)


@app.exception_handler(404)
async def Custom_404_handler(request: Request, _: Exception):
    """Custom 404 handler"""
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
