import os
from pathlib import Path

# Base Directory (The root of your project)
BASE_DIR = Path(__file__).resolve().parent.parent

# Data Paths
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
OUTPUT_DIR = BASE_DIR / "outputs"

# Create directories if they don't exist
for path in [RAW_DATA_DIR, PROCESSED_DATA_DIR, OUTPUT_DIR]:
    path.mkdir(parents=True, exist_ok=True)

# Dataset Column Constants (Mozilla Bugzilla specific)
TARGET_REGRESSION = "fix_time_hours"
TARGET_CLASSIFICATION = "severity_level"
TEXT_COLUMN = "bug_description"

# Model Hyperparameters
RANDOM_STATE = 42
TEST_SIZE = 0.2
PCA_COMPONENTS = 50
