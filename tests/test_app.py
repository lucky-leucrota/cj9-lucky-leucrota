import pytest
from httpx import AsyncClient

from src.app import app

baseUrl = "http://localhost:8000"  # Change the baseUrl after the production build.


@pytest.mark.anyio
async def test_root():
    """The test function for root/index."""
    async with AsyncClient(app=app, base_url=baseUrl) as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Bigger Applications!"}


@pytest.mark.anyio
async def test_example():
    """The test function for /example."""
    async with AsyncClient(app=app, base_url=baseUrl) as ac:
        response = await ac.get("/example/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
