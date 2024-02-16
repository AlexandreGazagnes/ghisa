"""
Load module
"""

import json
import pandas as pd


def save(ans, dest, out="json"):
    """Save the ans to the destination file."""

    if out == "json":

        with open(dest, "w") as f:
            # f.write(str(ans))

            json.dump(ans, f)
    if out == "csv":

        df = pd.DataFrame({"counts": ans})
        df.to_csv(dest, index=False)

    if out == "txt":
        with open(dest, "w") as f:
            f.write(str(ans))
