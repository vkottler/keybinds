# =====================================
# generator=datazen
# version=1.0.11
# hash=ddec513fc69ad08ef19b9e4817234c4e
# =====================================

"""
vbinds - Package definition for distribution.
"""

# internal
from vbinds import PKG_NAME, VERSION, DESCRIPTION
from mk.setup import setup


author_info = {"name": "Vaughn Kottler",
               "email": "vaughnkottler@gmail.com",
               "username": "vkottler"}
pkg_info = {"name": PKG_NAME, "version": VERSION, "description": DESCRIPTION}
setup(
    pkg_info,
    author_info,
    url_override="https://github.com/vkottler/keybinds/tree/master/wow",
    console_overrides=["bapi=vbinds.entry:main"],
)
