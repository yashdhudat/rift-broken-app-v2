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
    assert not is_admin(user)

def test_is_admin_true():
    from src.auth import is_admin
    user = {'role': 'admin'}
    assert is_admin(user)

def test_is_admin_missing_role():
    from src.auth import is_admin
    user = {}
    assert not is_admin(user) 

def test_is_admin_with_other_roles():
    from src.auth import is_admin
    user = {'role': 'other'}
    assert not is_admin(user)