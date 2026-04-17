"""A simple test file for the dummy_pkg."""

from dummy_pkg import add


def test_add():
    """Test for dummy_pkg.add"""
    assert add(2, 2) == 4
