"""
Utility functions for the app
"""

import subprocess
import logging
import os
from rich.logging import RichHandler
from pathlib import Path
from time import sleep


def get_logger() -> logging.Logger:
    """Get logger"""
    return logging.getLogger("pfred")
