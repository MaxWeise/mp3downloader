"""Testsuite for the Mp3Exporter.

Created: 31.05.2023
@author: Max Weise
"""

import os
import pathlib
import shutil
import unittest

from pydownloader.monad import Monad
from pydownloader.downloader import Mp3Exporter

class TestMp3Exporter(unittest.TestCase):

    def setUp(self):
        self.test_source = r"https://youtu.be/wOFVrjL-XBM"
        self.test_destination = pathlib.Path(r"./testing_byproducts")

    def test_export(self):
        """Test the export function of the Mp3Converter."""

        under_test = Mp3Exporter()
        actual: Monad = under_test.export(self.test_source, self.test_destination)

        self.assertTrue(actual.success)
        self.assertFalse(actual.error)

    def tearDown(self):
        if self.test_destination.is_dir():
            shutil.rmtree(self.test_destination)


if __name__ == "__main__":
    unittest.main()
