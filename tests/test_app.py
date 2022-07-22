from src.app import app

import pytest
from httpx import AsyncClient

baseUrl = "http://localhost:8000"


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url=baseUrl) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
