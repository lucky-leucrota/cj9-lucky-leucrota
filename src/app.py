from fastapi import FastAPI #, Request
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates

app = FastAPI(title="App", description="The app", version="0.1.0")
# templates = Jinja2Templates(directory="templates")
# app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return {"hello": "world"}


# @app.get("/index/", response_class=HTMLResponse)
# async def display_posts_by_id(request: Request):
#     return templates.TemplateResponse("template.html", {"request": request})
