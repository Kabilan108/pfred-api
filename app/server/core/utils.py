"""
Utility functions for the app
"""

import subprocess
import logging
import os

from pathlib import Path
from time import sleep


# get directories
RUN_DIR = Path(os.getenv("RUN_DIR", "/run"))
SCRIPTS_DIR = Path(os.getenv("SCRIPTS_DIR", "/scripts"))


def get_logger() -> logging.Logger:
    """Get logger"""
    return logging.getLogger("pfred")


