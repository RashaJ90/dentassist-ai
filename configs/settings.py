from pathlib import Path

# --------------------------------------------------
# Project root
# --------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# Data directories
# --------------------------------------------------

DATA_DIR = PROJECT_ROOT / "data"

RECORDINGS_DIR = DATA_DIR / "recordings"
SCRIPTS_DIR = DATA_DIR / "scripts"
TRANSCRIPTS_DIR = DATA_DIR / "transcripts"

# --------------------------------------------------
# Audio settings
# --------------------------------------------------

SUPPORTED_FORMATS = [
    ".m4a",
    ".mp3",
    ".aac",
    ".flac",
    ".ogg",
]

TARGET_AUDIO_FORMAT = "wav"
TARGET_SAMPLE_RATE = 16000
TARGET_CHANNELS = 1

# --------------------------------------------------
# Whisper / speech settings (future)
# --------------------------------------------------

WHISPER_MODEL = "base"

# --------------------------------------------------
# Logging
# --------------------------------------------------

LOGS_DIR = PROJECT_ROOT / "logs"

# --------------------------------------------------
# Future directories (for later phases)
# --------------------------------------------------

MODELS_DIR = PROJECT_ROOT / "models"
TEMP_DIR = PROJECT_ROOT / "tmp"