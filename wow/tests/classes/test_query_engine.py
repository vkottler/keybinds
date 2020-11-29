
"""
vbinds - Tests game-data queries.
"""

# internal
from tests.environment import get_new_cache

# module under test
from vbinds.classes.query_engine import QueryEngine


def test_query_engine_basic():
    """ TODO """

    engine = QueryEngine(get_new_cache())
    assert engine.static_query("playable-class/index") is not None
