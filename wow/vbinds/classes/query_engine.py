
"""
vbinds - TODO.
"""

# built-in
import logging
from typing import Optional

# third-party
import requests

# internal
from vbinds.enums import (
    Region, Locale, Namespace, get_namespace_str, get_query_str
)
from .token_engine import TokenEngine
from .cache import Cache


class QueryEngine(TokenEngine):
    """ TODO """

    log = logging.getLogger(__name__)

    def __init__(self, cache: Cache, region: Region = Region.US,
                 locale: Locale = Locale.en_US):
        """ TODO """

        super().__init__(cache, region)
        self.locale = locale

    def static_query(self, path: str,
                     path_root: str = "data/wow",
                     write_cache: bool = True) -> Optional[dict]:
        """ TODO """

        namespace_str = get_namespace_str(Namespace.Static, self.region)
        namespace_data = self.cache.get(namespace_str)
        full_path = "{}/{}".format(path_root, path)

        # return cached result if we alredy have it
        if full_path in namespace_data:
            return namespace_data[full_path]

        token = self.get_token()
        if token is None:
            return None

        args = {"locale": self.locale.value,
                "access_token": token,
                "namespace": namespace_str}
        query_str = get_query_str(self.region, full_path)
        QueryEngine.log.debug("query: '%s'", query_str)
        req = requests.get(query_str, params=args)

        # make sure we got a valid response
        if req.status_code != requests.codes["ok"]:
            TokenEngine.log.error("error querying '%s': %s", full_path,
                                  req.json())
            return None

        # write the cached result
        namespace_data[full_path] = req.json()
        if write_cache:
            self.cache.save()
        TokenEngine.log.info(namespace_data[full_path])
        return namespace_data[full_path]
