
"""
vbinds - Tests for token retrieval.
"""

# internal
from tests.environment import get_new_cache

# module under test
from vbinds.classes.token_engine import TokenEngine


def test_token_engine_basic():
    """
    Get a new token, then make sure that the cached token is used next time.
    """

    engine = TokenEngine(get_new_cache())
    assert engine.get_token() is not None
    assert engine.get_token() is not None
    engine.cache.clean()
