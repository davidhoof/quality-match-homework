from unittest import TestCase
from analysis.parser.project_parser import ProjectParser


class TestProjectParser(TestCase):
    JSON_PATH = "G:\\Users\\David\\QualityMatch\\anonymized_project.json"
    NOT_JSON_PATH = "G:\\Users\\David\\QualityMatch\\[EXT] Homework - (bicycle project crowd evaluation).pdf"

    def test_project_parser_task_path(self):
        self.assertRaises(ValueError, ProjectParser, self.JSON_PATH, dict())

    def test_project_parser_json_path(self):
        self.assertRaises(FileNotFoundError, ProjectParser, "NotAPath")

    def test_project_parser_not_json_path(self):
        self.assertRaises(ValueError, ProjectParser, self.NOT_JSON_PATH)
