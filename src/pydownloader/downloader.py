"""Define the interface for exporter classes.

Created: 31.05.2023
@author: Max Weise
"""

import pathlib
from typing import Protocol

from pydownloader.monad import Monad


class VideoToAudioExporter(Protocol):
    """Define the interface for audio exporters.

    This class is intended as a base class and should not be instantiated.
    """

    def export(self, source_url: str, destination_folder: pathlib.Path) -> Monad:
        """Save the given url as audio.

        Args:
            source_url: The object to be converted.
            destination_folder: The path where the audio file is saved.

        Returns:
            Monad: Wrapper object for success and error values.
        """
        raise NotImplementedError(
            f"This method is not implemented for the type {self}")


class Mp3Exporter:
    """Covert a video given by a url to mp3 format."""

    def export(self, source_url, destination_folder: pathlib.Path) -> Monad:
        """Save the given video as audio.

        Args:
            source_url: The object to be converted.

        Returns:
            Monad: Wrapper object for success and error values.
        """
        ret: bool = True
        err: Exception | None = None

        return Monad(ret, err)
