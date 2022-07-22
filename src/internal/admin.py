from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin():
    """The admin thing this is also something we will after some time."""
    return {"message": "Admin getting schwifty"}
