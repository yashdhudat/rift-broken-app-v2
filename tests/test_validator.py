import pytest
import sys
sys.path.insert(0, '.')

def test_validate_email_valid():
    # Will fail due to syntax error in validator.py
    from src.validator import validate_email
    assert validate_email("test@example.com") == True

def test_validate_email_invalid():
    from src.validator import validate_email
    assert validate_email("notanemail") == False
