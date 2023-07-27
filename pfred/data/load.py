"""load - load data from included files"""

import os


def _data_dir():
    """Return path to package data directory"""
    return os.path.join(os.path.dirname(__file__), "files")


def generic_loader():
    """Generic data loader"""

    path = os.path.join(_data_dir(), "generic.txt")
