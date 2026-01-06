from app import greet

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("Docker") == "Hello, Docker!"
