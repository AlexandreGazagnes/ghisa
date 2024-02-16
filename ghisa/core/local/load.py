"""
Load module
"""

import json

import pandas as pd


def save(ans, dest):
    """Save the ans to the destination file."""

    if "json" in dest:
        with open(dest, "w") as f:
            json.dump(ans, f)

    elif "csv" in dest:
        df = pd.DataFrame({"counts": ans})
        df.to_csv(dest, index=False)

    elif "txt" in dest:
        with open(dest, "w") as f:
            f.write(str(ans))

    else:
        raise ValueError(f"Expected {dest}  extension to be in ['json', 'csv', 'txt']")
