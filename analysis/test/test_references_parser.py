from unittest import TestCase

import pandas as pd

from analysis.parser.references_parser import ReferenceParser


class TestReferenceParser(TestCase):
    JSON_PATH = "G:\\Users\\David\\QualityMatch\\anonymized_project.json"
    NOT_JSON_PATH = "G:\\Users\\David\\QualityMatch\\[EXT] Homework - (bicycle project crowd evaluation).pdf"

    def test_reference_parser_json_path(self):
        self.assertRaises(FileNotFoundError, ReferenceParser, "NotAPath")

    def test_reference_parser_not_json_path(self):
        self.assertRaises(ValueError, ReferenceParser, self.NOT_JSON_PATH)

    def test_reference_parser_to_dataframe(self):
        reference_parser = ReferenceParser(self.JSON_PATH)
        df = reference_parser.to_dataframe()
        self.assertEqual(type(df), pd.DataFrame)

    def test_reference_parser_to_dataframe_cache(self):
        reference_parser = ReferenceParser(self.JSON_PATH)

        df = reference_parser.to_dataframe(cache=True)
        df2 = reference_parser.to_dataframe(cache=True)

        self.assertTrue(df is df2)

        df = reference_parser.to_dataframe(cache=False)
        df2 = reference_parser.to_dataframe(cache=False)
        self.assertFalse(df is df2)


