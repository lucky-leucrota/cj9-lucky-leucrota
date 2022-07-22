from fastapi import APIRouter  # , Depends, HTTPException

# from ..dependencies import get_token_header

# We will lay off the tokens for now.


router = APIRouter(
    prefix="/example",
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def index():
    """The root of the app"""
    return {"hello": "world"}
