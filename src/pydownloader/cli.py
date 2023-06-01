"""Command line interface to download YouTube Videos.

This file defines an interface to interact with the converter obejcts.
Run this file to download videos from YouTube and convert them to a desired
format.

Created: 01.06.2023
@author: Max Weise
"""

from enum import Enum
import pathlib

from pydownloader import downloader
from pydownloader import monad
from monad import Monad


SOURCE_URL: str = r"https://youtu.be/o1SltokvFd4"
DESTINATION_FOLDER = pathlib.Path(r"C:\Users\fenci\Downloads")


class _SuportedAudioFormats(Enum):
    MP3 = "mp3"


def _register_audio_exporters() -> dict[_SuportedAudioFormats, downloader.VideoToAudioExporter]:
    ret: dict[_SuportedAudioFormats, downloader.VideoToAudioExporter] = {}
    ret[_SuportedAudioFormats.MP3] = downloader.Mp3Exporter()
    return ret


def main():
    """Run the main script of the programm."""

    audio_exporters: dict[_SuportedAudioFormats, downloader.VideoToAudioExporter] = _register_audio_exporters()

    exporter: downloader.Mp3Exporter | None = audio_exporters.get(_SuportedAudioFormats.MP3, None)

    if not exporter:
        print("The given exporter is not recognized")
        exit()

    return_monad: Monad = exporter.export(SOURCE_URL, DESTINATION_FOLDER)

    if return_monad.success:
        print("=== Download Successfull ===")
    else:
        print(f"While downloading the given url, this exception occured:\n{return_monad.error}")


if __name__ == "__main__":
    main()
