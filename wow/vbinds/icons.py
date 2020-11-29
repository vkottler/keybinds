
"""
vtools - Functions for downloading in-game icon image files.
"""

# built-in
from enum import Enum
import os
import logging
from typing import Optional

# third-party
import requests

LOG = logging.getLogger(__name__)


class IconSize(Enum):
    """
    Required parameter for retrieving in-game icons. See:
    https://us.battle.net/forums/en/bnet/topic/20755767469
    """

    SMALL = 18
    MEDIUM = 36
    LARGE = 56


def get_icon_url(name: str, size: IconSize):
    """ Get the web-url for a named icon. """

    file_name = "{}.jpg".format(name)
    icon_url_fmt = "http://media.blizzard.com/wow/icons/{}/{}"
    return icon_url_fmt.format(str(size.value), file_name)


def get_icon(name: str, dest_root: str = ".",
             size: IconSize = IconSize.LARGE) -> Optional[str]:
    """
    Write an image file to disk for a given icon. Return the path written.
    """

    # start the icon-query stream
    req = requests.get(get_icon_url(name, size), stream=True)
    if req.status_code != requests.codes["ok"]:
        LOG.error("error getting icon '%s': %d %s", name, req.status_code,
                  req.text)
        return None

    # write the file contents
    dest_dir = os.path.join(dest_root, str(size.value))
    os.makedirs(dest_dir, exist_ok=True)
    full_path = os.path.join(dest_dir, "{}.jpg".format(name))
    with open(full_path, "wb") as img_fd:
        for chunk in req.iter_content(chunk_size=256):
            img_fd.write(chunk)

    LOG.info("wrote icon '%s' to '%s'", name, full_path)
    return full_path
