from fastapi import FastAPI  # , Request, Depends

from .routers import main

# from .dependencies import get_query_token, get_token_header
# from .internal import admin


app = FastAPI(title="App", description="The app", version="0.1.0")

app.include_router(main.router)
# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     dependencies=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )


@app.get("/")
async def root():
    """The root"""
    return {"message": "Hello Bigger Applications!"}
