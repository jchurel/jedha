"""
    All util functions are here
"""
import pandas as pd

def hello(name):
    print(f"Hello {name}")


def convert_size_bytes(size_bytes):
    """
    Converts a size in bytes to a human readable string using SI units.
    """
    import math
    import sys

    if not isinstance(size_bytes, int):
        size_bytes = sys.getsizeof(size_bytes)

    if size_bytes == 0:
        return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = size_bytes / p
    x = round(s)
    return "%s%s" % (x, size_name[i])

def missing_values(df):
    missing_values = pd.DataFrame.from_dict(
    {c: df.filter(df[c].isNull()).count() for c in df.columns},
    orient='index', columns=['missing values']
    )
