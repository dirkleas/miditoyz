# Copyright (c) 2023 Dirk Leas
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import unittest, shutil, duckdb
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader

spec = spec_from_loader("miditoyz", SourceFileLoader("miditoyz", "miditoyz"))
miditoyz = module_from_spec(spec)
spec.loader.exec_module(miditoyz)

# shutil.rmtree("/tmp/songs", ignore_errors=True)
# miditoyz.init("test", "/tmp/songs")


class TestMiditoyzCommands(unittest.TestCase):
    def test_db_broken_songs(self):
        broken_songs = (
            duckdb.connect("/tmp/songs/catalog.db")
            .execute(
                "select count(*) from catalog where broken_mido is true or broken_music21 is true"
            )
            .fetchone()[0]
        )
        self.assertTrue(broken_songs == 2, "expected 2 broken songs")


if __name__ == "__main__":
    unittest.main()
