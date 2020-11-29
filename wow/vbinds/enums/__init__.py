
"""
vbinds - Useful enumeration definitions.
"""

# built-in
from enum import Enum


class Region(Enum):
    """
    See "Regions" table at:
    https://develop.battle.net/documentation/guides/regionality-partitions-and-localization
    """

    US = "us"
    EU = "eu"
    KR = "kr"
    TW = "tw"
    CN = "cn"


class Namespace(Enum):
    """
    See "World of Warcraft Namespaces" table at:
    https://develop.battle.net/documentation/guides/game-data-apis-wow-namespaces
    """

    Static = "static-{0}"
    Dynamic = "dynamic-{0}"
    Profile = "profile-{0}"


def get_query_str(region: Region, query_str: str) -> str:
    """ Build a query URL based on the region and the query sub-String. """

    query_format_str = "https://gateway.battlenet.com.{0}/{1}"
    if Region != Region.CN:
        query_format_str = "https://{0}.api.blizzard.com/{1}"
    return query_format_str.format(region.value, query_str)


def get_namespace_str(namespace: Namespace, region: Region):
    """ Get a fully-qualified namespace String. """

    return namespace.value.format(region)
