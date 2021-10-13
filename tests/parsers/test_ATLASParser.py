import os
from fastavro import reader
import unittest

from survey_parser_plugins.parsers import ATLASParser, ZTFParser

FILE_PATH = os.path.dirname(__file__)
ATLAS_DATA_PATH = os.path.join(FILE_PATH, "../../notebooks/data/ATLAS_samples")
ZTF_DATA_PATH = os.path.join(FILE_PATH, "../../notebooks/data/ZTF_samples")


def get_content(file_path):
    with open(file_path, "rb") as f:
        content = reader(f).next()
    return content


class TestATLASParser(unittest.TestCase):
    def setUp(self) -> None:
        self._atlas_sample = [get_content(os.path.join(ATLAS_DATA_PATH, f)) for f in os.listdir(ATLAS_DATA_PATH)]
        self._ztf_sample = [get_content(os.path.join(ZTF_DATA_PATH, f)) for f in os.listdir(ZTF_DATA_PATH)]

    def test_can_parse(self):
        atlas_message = self._atlas_sample[0]
        response = ATLASParser.can_parse(atlas_message)
        self.assertTrue(response)

    def test_cant_parse(self):
        ztf_message = self._ztf_sample[0]
        response = ATLASParser.can_parse(ztf_message)
        self.assertFalse(response)

    def test_parse(self):
        pass

    def test_bad_message(self):
        pass

    def test_get_source(self):
        pass