"""
read a csv without knowing the delimiter in advance.
works for tab, comma, semicolon, pipe. header row assumed.
"""

import csv
import io


def read(path_or_str, sample_size=4096):
    if hasattr(path_or_str, "read"):
        fh = path_or_str
    elif "\n" in path_or_str[:200]:
        fh = io.StringIO(path_or_str)
    else:
        fh = open(path_or_str, newline="")

    sample = fh.read(sample_size)
    fh.seek(0)
    dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
    return list(csv.DictReader(fh, dialect=dialect))
