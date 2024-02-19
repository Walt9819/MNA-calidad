"""
Check if file exists
"""

import os


def check_file_existence(path):
    """
    Check if file exists
    """
    return os.path.exists(path)


def get_values(i, line):
    """
    Get values from a line
    """
    try:
        v = line.split(",")
        return v[0], v[1], v[2]
    except ValueError:
        print(f"Line {i} invalid value {(line)}. Skipping.")
        return None
