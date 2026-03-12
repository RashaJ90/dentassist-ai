from pathlib import Path
from pydub import AudioSegment

from configs.settings import (
    RECORDINGS_DIR,
    SUPPORTED_FORMATS,
    TARGET_AUDIO_FORMAT,
    TARGET_SAMPLE_RATE,
    TARGET_CHANNELS,
)


def convert_file(file_path: Path):
    output_file = file_path.with_suffix(f".{TARGET_AUDIO_FORMAT}")

    print(f"Converting {file_path.name} -> {output_file.name}")

    audio = AudioSegment.from_file(file_path)

    audio = audio.set_frame_rate(TARGET_SAMPLE_RATE)
    audio = audio.set_channels(TARGET_CHANNELS)

    audio.export(output_file, format=TARGET_AUDIO_FORMAT)

    print(f"Saved: {output_file}")


def main():

    if not RECORDINGS_DIR.exists():
        print("Recordings directory does not exist.")
        return

    files = list(RECORDINGS_DIR.iterdir())

    if not files:
        print("No files found in recordings directory.")
        return

    for file in files:

        if file.suffix.lower() in SUPPORTED_FORMATS:
            convert_file(file)

    print("Conversion process finished.")


if __name__ == "__main__":
    main()