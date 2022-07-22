from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header()):
    """Gets the token in the header"""
    if x_token != "admin-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    """Gets the query token in the header."""
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")
