"""Define the interface for exporter classes.

Created: 31.05.2023
@author: Max Weise
"""

import pathlib
from pathlib import Path
import os
import shutil
from typing import Protocol, Any

import moviepy
import moviepy.editor
import pytube


class VideoToAudioExporter(Protocol):
    """Define the interface for audio exporters.

    This class is intended as a base class and should not be instantiated.
    """

    def export(self, source_url: str, destination_folder: pathlib.Path) -> Any:
        """Save the given url as audio.

        Args:
            source_url: The object to be converted.
            destination_folder: The path where the audio file is saved.

        Returns:
            Monad: Wrapper object for success and error values.
        """
        raise NotImplementedError(f"This method is not implemented for the type {self}")


class Mp3Exporter:
    """Covert a video given by a url to mp3 format."""

    def _download_video(self, source_url: str) -> Path:
        video = pytube.YouTube(source_url)
        video_stream = video.streams.filter(only_audio=True).first()
        path_to_file = video_stream.download()
        return pathlib.Path(path_to_file)

    def _convert_video_to_audio(self, video_file: Path) -> bool:
        try:
            absolute_path = video_file.absolute()
            _video_file: str = absolute_path.as_posix()
            _video_file = _video_file.replace(" ", "_")
            base, ext = _video_file.split(".")
            _video_file = f"{base}.mp3"

            video_file.rename(_video_file)
            # print(_video_file, type(_video_file))
        except Exception as e:
            print(f"While converting from mp4 to mp3, this exception occured: {e}")
            return False
        return True

    # TODO: when path does not exist or causes an error
    # Raise an exception which can be handled in the main programm
    def export(self, source_url) -> bool | None:
        """Save the given video as audio.

        Args:
            source_url: The object to be converted.

        Returns:
            Path: Path to the downloaded mp3 file.
        """
        ret: bool = False
        try:
            video_file: Path = self._download_video(source_url)
            ret = self._convert_video_to_audio(video_file)
        except Exception as e:
            # TODO: Re-Raise exception
            print(e)

        return ret
