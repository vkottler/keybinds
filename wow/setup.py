# =====================================
# generator=datazen
# version=1.7.7
# hash=d32e9320e48537021823a5a8e1437c32
# =====================================

"""
vbinds - Package definition for distribution.
"""

# third-party
from vmklib.setup import setup

# internal
from vbinds import PKG_NAME, VERSION, DESCRIPTION


author_info = {
    "name": "Vaughn Kottler",
    "email": "vaughnkottler@gmail.com",
    "username": "vkottler",
}
pkg_info = {
    "name": PKG_NAME,
    "version": VERSION,
    "description": DESCRIPTION,
    "versions": [
        "3.6",
        "3.7",
        "3.8",
    ],
}
setup(
    pkg_info,
    author_info,
    url_override="https://github.com/vkottler/keybinds/tree/master/wow",
    console_overrides=["bapi=vbinds.entry:main"],
)
