# """
# Integration test the ghisa class.
# """

# import pytest


# from ghisa.core.ghisa import Ghisa
# from ghisa.logger import logger

# from ghisa.config import config


# class TestIntergrationGhisa:
#     """Test the ghisa class."""

#     def test___init__(self):
#         Ghisa(test_mode=True)

#     # def test_crawl_repo(self):

#     #     gh = Ghisa(test_mode=True)

#     #     imports = gh.crawl_repo("https://github.com/MentalDeFer972/project2py-ocr")

#     #     logging.info(imports)

#     def test_crawl_repo(self):

#         gh = Ghisa(test_mode=True)

#         url = "https://github.com/AlexandreGazagnes/"
#         dict_ = gh.craw_profile(url)

#         logging.info(dict_)
