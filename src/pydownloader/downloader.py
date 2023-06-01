"""Define the interface for exporter classes.

Created: 31.05.2023
@author: Max Weise
"""

import pathlib
import os
from typing import Protocol, Any

import pytube

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

    def _save_file_to_disk(self, file: Any) -> Monad:
        ret: bool = True
        error: Exception | None = None
        base, ext = os.path.splitext(file)
        new_file = base + '.mp3'
        # print(new_file)
        os.rename(file, new_file)
        return Monad(ret, error)

    def export(self, source_url, destination_folder: pathlib.Path) -> Monad:
        """Save the given video as audio.

        Args:
            source_url: The object to be converted.

        Returns:
            Monad: Wrapper object for success and error values.
        """
        ret: bool = True
        err: Exception | None = None

        try:
            video = pytube.YouTube(source_url)
            audio = video.streams.filter(only_audio=True).first()
            saved_file = audio.download(output_path=destination_folder)
        except Exception as e:
            ret = False
            err = e
        else:
            return_monad = self._save_file_to_disk(saved_file)
            ret = return_monad.success
            err = return_monad.error

        return Monad(ret, err)
