from pathlib import Path
from pydub import AudioSegment
import argparse

from configs.settings import (
    RECORDINGS_DIR,
    SUPPORTED_FORMATS,
    TARGET_AUDIO_FORMAT,
    TARGET_SAMPLE_RATE,
    TARGET_CHANNELS,
)
import scripts


def convert_file(file_path: Path, sample_rate: int, channels: int, audio_format: str):
    output_file = file_path.with_suffix(f".{audio_format}")

    print(f"Converting {file_path.name} -> {output_file.name}")

    audio = AudioSegment.from_file(file_path)
    audio = audio.set_frame_rate(sample_rate)
    audio = audio.set_channels(channels)
    audio.export(output_file, format=audio_format)

    print(f"Saved: {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert audio files to a target format."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=RECORDINGS_DIR,
        help=f"Directory containing audio files to convert (default: {RECORDINGS_DIR})",
    )
    parser.add_argument(
        "--format",
        type=str,
        default=TARGET_AUDIO_FORMAT,
        help=f"Target audio format (default: {TARGET_AUDIO_FORMAT})",
    )
    parser.add_argument(
        "--sample-rate",
        type=int,
        default=TARGET_SAMPLE_RATE,
        help=f"Target sample rate in Hz (default: {TARGET_SAMPLE_RATE})",
    )
    parser.add_argument(
        "--channels",
        type=int,
        default=TARGET_CHANNELS,
        choices=[1, 2],
        help=f"Number of audio channels - 1 (mono) or 2 (stereo) (default: {TARGET_CHANNELS})",
    )
    parser.add_argument(
        "--supported-formats",
        nargs="+",
        default=SUPPORTED_FORMATS,
        help=f"List of input formats to process (default: {SUPPORTED_FORMATS})",
    )

    args = parser.parse_args()

    if not args.input_dir.exists():
        print(f"Recordings directory '{args.input_dir}' does not exist.")
        return

    files = list(args.input_dir.iterdir())

    if not files:
        print("No files found in recordings directory.")
        return

    for file in files:
        if file.suffix.lower().lstrip(".") in args.supported_formats:
            convert_file(file, args.sample_rate, args.channels, args.format)

    print("Conversion process finished.")


if __name__ == "__main__":
    main()




# Use all defaults from settings
## python -m scripts.convert_to_wav

# Override the input directory
## python -m scripts.convert_to_wav --input-dir /path/to/audio

# Convert to mp3 at 44100Hz stereo
## python -m scripts.convert_to_wav --format mp3 --sample-rate 44100 --channels 2

# Only process specific formats
## python -m scripts.convert_to_wav --supported-formats mp3 ogg

# See all options
## python -m scripts.convert_to_wav --help