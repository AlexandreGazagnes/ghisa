"""
Test the extract module
"""

import os, sys
import pytest

from ghisa.core.helpers import *


class TestExtractFromImportLine:

    def test_extract_from_import_line_1(self):

        txt = "from ghisa.core.defaults import DEFAULT_CONFIG"
        assert extract_from_import_line(txt) == "ghisa"

    def test_extract_from_import_line_2(self):

        txt = "import os"
        assert extract_from_import_line(txt) == "os"

    def test_extract_from_import_line_3(self):

        txt = "import os, sys"
        assert extract_from_import_line(txt) == ["os", "sys"]

    def test_extract_from_import_line_4(self):

        txt = "import matplotlib.pyplot as plt"
        assert extract_from_import_line(txt) == "matplotlib"
