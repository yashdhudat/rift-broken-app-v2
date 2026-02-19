import pytest
import sys
sys.path.insert(0, '.')
from src.utils import get_timestamp, flatten

def test_get_timestamp():
    ts = get_timestamp()
    assert isinstance(ts, str)

def test_flatten():
    assert flatten([[1,2],[3,4]]) == [1,2,3,4]

def test_flatten_empty():
    assert flatten([]) == []
