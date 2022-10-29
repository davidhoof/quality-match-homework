from unittest import TestCase

from analysis.parser.references_parser import ReferenceParser


class TestReferenceParser(TestCase):
    JSON_PATH = "G:\\Users\\David\\QualityMatch\\anonymized_project.json"
    NOT_JSON_PATH = "G:\\Users\\David\\QualityMatch\\[EXT] Homework - (bicycle project crowd evaluation).pdf"

    def test_project_parser_json_path(self):
        self.assertRaises(FileNotFoundError, ReferenceParser, "NotAPath")

    def test_project_parser_not_json_path(self):
        self.assertRaises(ValueError, ReferenceParser, self.NOT_JSON_PATH)
