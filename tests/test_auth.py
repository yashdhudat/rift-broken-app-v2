import pytest
import sys
sys.path.insert(0, '.')

def test_generate_token():
    from src.auth import generate_token
    token = generate_token(1)
    assert len(token) == 32

def test_is_admin_false():
    from src.auth import is_admin
    user = {'role': 'user'}
    assert is_admin(user) == False