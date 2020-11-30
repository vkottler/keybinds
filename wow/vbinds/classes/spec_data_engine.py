
"""
vbinds - A query extension for querying class-specialization data.
"""

# built-in
from typing import Optional

# internal
from .query_engine import QueryEngine


class SpecDataEngine(QueryEngine):
    """ Exposes 'Playable Specialization API' queries. """

    def get_specs(self, should_print: bool = False) -> Optional[dict]:
        """ Exposes the 'Playable Specializations Index' API call. """

        return self.static_query("playable-specialization/index", should_print)
