
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
