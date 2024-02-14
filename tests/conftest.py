"""
Fixtures for the tests
"""

import os

import pytest

from ghisa.logger import logger
from ghisa.core.ghisa import ghisa


# VIDEO_URL = "https://www.youtube.com/watch?v=9diaThxYnKA"
# VIDEO_ID = "V62oKsHdsLU"
# VIDEO_QUERY = "jo l'rigolo"


# def read_file(fn: str) -> str:
#     """Read a fn"""

#     base = "docs/assets/tests"

#     pwd = os.getcwd()
#     logger.warning(f"pwd: {pwd}")
#     logger.warning(f"ls: {os.listdir(pwd)}")

#     _fn = os.path.join(pwd, base, fn)

#     if not os.path.exists(_fn):
#         raise FileNotFoundError(f"File not found: {_fn}")

#     with open(_fn, "r") as _fn:
#         out = _fn.readlines()

#     if not isinstance(out, list):
#         raise ValueError(f"Expected list, got {type(out)}")

#     if not len(out):
#         raise ValueError(f"Empty file: {_fn}")

#     return out


# @pytest.fixture
# def ghisa() -> ghisa:
#     """Lod an ghisa instance"""

#     return ghisa()


# # @pytest.fixture
# # def list_ids() -> list:
# #     """List of video ids"""

# #     pwd = os.getcwd()
# #     logger.warning(f"pwd: {pwd}")
# #     logger.warning(f"ls: {os.listdir(pwd)}")

# #     fn = "list_ids.txt"

# #     return read_file(fn)


# # @pytest.fixture
# # def list_urls() -> list:
# #     """List of video urls"""

# #     pwd = os.getcwd()
# #     logger.warning(f"pwd: {pwd}")
# #     logger.warning(f"ls: {os.listdir(pwd)}")

# #     fn = "list_urls.txt"

# #     return read_file(fn)


# # @pytest.fixture
# # def list_queries() -> list:
# #     """List of video queries"""

# # fn = "list_queries.txt"

# # return read_file(fn)


# def pytest_sessionstart(session):
#     """
#     Called after the Session object has been created and
#     before performing collection and entering the run test loop.
#     """

#     if os.path.exists(ghisa.DEFAULT_TMP):
#         for file in os.listdir(ghisa.DEFAULT_TMP):
#             os.remove(ghisa.DEFAULT_TMP + file)
#         os.rmdir(ghisa.DEFAULT_TMP)

#     if not os.path.exists(ghisa.DEFAULT_TMP):
#         os.makedirs(ghisa.DEFAULT_TMP)
