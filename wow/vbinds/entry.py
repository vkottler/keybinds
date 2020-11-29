
"""
vbinds - Package's command-line entry-point.
"""

# built-in
import argparse
import logging
import os
from typing import List

# internal
from vbinds.classes.icon_cache import IconCache
from vbinds.classes.engine import engine_from_output_root
from . import DESCRIPTION


def main(argv: List[str]) -> int:
    """ Program entry-point. """

    result = 0

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="set to increase logging verbosity")
    parser.add_argument("-o", "--out-dir", default=os.getcwd(),
                        help="root directory for program outputs")

    try:
        args = parser.parse_args(argv[1:])
        args.out_dir = os.path.abspath(args.out_dir)

        # initialize logging
        log_level = logging.DEBUG if args.verbose else logging.INFO
        logging.basicConfig(level=log_level,
                            format=("%(name)-30s - %(levelname)-8s - "
                                    "%(message)s"))

        # initialize an icon cache and query engine
        icon_cache = IconCache(os.path.join(args.out_dir, "icons"))
        engine = engine_from_output_root(args.out_dir)

        icon_cache.get("spell_frost_frostshock")

        classes = engine.get_classes()
        if classes is not None:
            for class_data in classes:
                engine.get_class(class_data["id"], True)

    except SystemExit as exc:
        result = 1
        if exc.code is not None:
            result = exc.code

    return result
