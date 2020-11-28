
"""
vbinds - A simple data cache with file-system backing.
"""

# built-in
import json
import os
import shutil

# internal
from . import DEFAULT_CACHE


class Cache:
    """ Class for storing dictionary data backed by JSON on disk. """

    def __init__(self, cache_dir: str = DEFAULT_CACHE):
        """ Load an existing cache or construct a new one. """

        self.dir = cache_dir
        if not os.path.isdir(self.dir):
            os.makedirs(self.dir)
        self.data = defaultdict(dict)
        self.load()

    def save(self) -> None:
        """ Write each data key to a JSON file in the cache. """

        for key, data in self.data.items():
            full_path = os.path.join(self.dir, "{}.json".format(key))
            with open(full_path, "w") as out_file:
                out_file.write(json.dumps(data))

    def load(self) -> None:
        """ Load each JSON file in the cache as data. """

        for filename in os.listdir(self.dir):
            with open(filename) as in_file:
                key = filename.replace(".json", "")
                self.data[key] = json.loads(in_file.read())

    def clean(self) -> None:
        """ Delete the cahce on disk and reset data. """

        shutil.rmtree(self.dir)
        os.makedirs(self.dir)
        self.data = defaultdict(dict)

    def get(self, key: str) -> dict:
        """ Get an existing (or new) top-level key's data. """

        return self.data[key]
