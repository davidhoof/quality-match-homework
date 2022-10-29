from unittest import TestCase

from analysis.image.input_display import InputDisplay
from analysis.parser.project_parser import ProjectParser


class TestInputDisplay(TestCase):
    JSON_PATH = "G:\\Users\\David\\QualityMatch\\anonymized_project.json"

    def test_plot_images(self):
        project_parser_ = ProjectParser(self.JSON_PATH)
        input_display_ = InputDisplay(project_parser_)

        df = project_parser_.to_dataframe()

        cant_solve_sample_input_ids = list(df[(df['task_output.cant_solve'] == True)]['project_node_input_id'].unique())

        input_display_.plot_images(cant_solve_sample_input_ids, rows=3, cols=3, figsize=(20, 20))
