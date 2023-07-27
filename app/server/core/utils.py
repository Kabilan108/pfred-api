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


# create logger
logger = logging.getLogger("pfred")


# public static boolean runCommandThroughShell(String command, String directory)
def run_shell(command: str, directory: str) -> bool:
    """Run a command in the shell"""

    logger.warning("Running command: %s in %s", command, directory)

    try:
        subprocess.run(f"cd {directory} && {command}", shell=True, check=True)
    except subprocess.CalledProcessError as exc:
        logger.error("Error executing command in bash shell: %s", exc)
        return False

    return True
