import pytest

from src.app import app

baseUrl = "http://localhost:8000"  # Change the baseUrl after the production build.

def test_test():
    "Just testing the test"
    assert "hello"=="hello"