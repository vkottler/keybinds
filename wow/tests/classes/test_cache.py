
"""
vbinds - Tests for the data cache.
"""

# internal
import tempfile

# module under test
from vbinds.classes.cache import Cache


def test_cache_basic():
    """ Test that a second cache-load will have the correct data. """

    temp_cache = tempfile.mkdtemp()

    cache = Cache(temp_cache)
    test_data = cache.get("test")
    test_data["a"] = "a"
    test_data["b"] = "b"
    test_data["c"] = "c"
    cache.save()

    new_cache = Cache(temp_cache)
    compare_data = new_cache.get("test")
    assert compare_data["a"] == "a"
    assert compare_data["b"] == "b"
    assert compare_data["c"] == "c"

    new_cache.clean()
