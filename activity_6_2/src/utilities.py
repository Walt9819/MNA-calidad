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
        # Check if line is not empty (or contains only spaces or tabs or newlines)
        if line.strip() != "":
            v = line.replace("\n", "").split(",")
            return v[0], v[1], v[2]
        else:
            print(f"Line {i} is empty. Skipping.")
            return None
    except ValueError:
        print(f"Line {i} invalid value {(line)}. Skipping.")
        return None
