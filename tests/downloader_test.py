"""Testsuite for the Mp3Exporter.

Created: 31.05.2023
@author: Max Weise
"""

import os
import pathlib
import shutil
import unittest

from typing import Any
from pathlib import Path

from pydownloader.downloader import Mp3Exporter


class TestMp3Exporter(unittest.TestCase):
    def setUp(self):
        self.test_source: str = r"https://youtu.be/wOFVrjL-XBM"

    # TODO: Mock the call to pytube.download
    # Either verify and / or mock it completely
    def test_export(self):
        """Test the export function of the Mp3Converter."""

        under_test = Mp3Exporter()
        actual: bool | None = under_test.export(self.test_source)

        self.assertTrue(actual)

    def test_export_UrlDoesNotExist(self):
        """Test the export function of the Mp3Converter."""
        random_url: str = r"https://wwww.doesNotExist.random"

        under_test = Mp3Exporter()
        actual: bool | None = under_test.export(random_url)

        self.assertFalse(actual)

    def tearDown(self):
        _file = pathlib.Path(r"Navi_Hey_listen_all_sounds.mp3")
        if _file.is_file():
            os.remove(_file)


if __name__ == "__main__":
    unittest.main()
