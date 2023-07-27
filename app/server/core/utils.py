"""
Utility functions for the app
"""

import subprocess
import logging
import os

from pathlib import Path


# get directories
RUNS_DIR = Path(os.getenv("RUN_DIR", "/runs"))
SCRIPTS_DIR = Path(os.getenv("SCRIPTS_DIR", "/scripts"))


# setup logging
def get_logger() -> logging.Logger:
    """Get logger"""
    return logging.getLogger("pfred")
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


# public static String readFileAsString(String filePath) throws java.io.IOException 
def read_file(filepath: str) -> str:
    """Read a file and return contents as a string"""

    logger.warning("Reading file: %s", filepath)

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except IOError as exc:
        logger.error("Error reading file: %s", exc)
        return ""


# public static void saveStringAsFile(String filePath, String contents)
def save_file(filepath: str, contents: str) -> None:
    """Save a file with contents"""

    logger.warning("Saving file: %s", filepath)

    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(contents)
    except IOError as exc:
        logger.error("Error saving file: %s", exc)


# public static boolean copyFile(String filePath, String targetDirectory)
def copyfile(filepath: str, target_dir: str) -> bool:
    """Copy a file to a directory"""

    logger.warning("Copying file: %s to %s", filepath, target_dir)

    try:
        subprocess.run(f"cp {filepath} {target_dir}", shell=True, check=True)
    except subprocess.CalledProcessError as exc:
        logger.error("Error copying file: %s", exc)
        return False

    return True


# public static String prepareRunDir(String runName)
def create_run_dir(run_name: str) -> str:
    """Prepare the run directory"""

    logger.warning("Preparing run directory: %s", run_name)

    path = Path(RUNS_DIR) / run_name
    path.mkdir(parents=True, exist_ok=True)
    return str(path)


# public static boolean removeDir(String dirPath)
def remove_dir(dir_path: str) -> bool:
    """Remove a directory"""

    logger.warning("Removing directory: %s", dir_path)

    try:
        subprocess.run(f"rm -rf {dir_path}", shell=True, check=True)
    except subprocess.CalledProcessError as exc:
        logger.error("Error removing directory: %s", exc)
        return False

    return True

# public static String getRunDir()
def get_runs_dir() -> str:
    """Get the runs directory"""
    return str(RUNS_DIR)


# public static String getScriptsDir()
def get_scripts_dir() -> str:
    """Get the scripts directory"""
    return str(SCRIPTS_DIR)
