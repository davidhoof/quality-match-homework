import matplotlib.pyplot as plt
from imageio import imread

from analysis.parser.project_parser import ProjectParser


class InputDisplay:
    SUPPORTED_INPUT_TYPES = ['image_url']

    def __init__(self, project_parser: ProjectParser):
        self.__project_parser = project_parser

    def plot_images(self, input_ids, rows, cols, **kwargs):
        assert type(rows) is int
        assert type(cols) is int

        image_urls = self.__extract_urls(input_ids)

        fig, ax = plt.subplots(rows, cols, **kwargs)

        for idx, ax_ in enumerate(ax.flatten()):
            a = imread(image_urls[idx])
            ax_.set_title(input_ids[idx])
            ax_.imshow(a)
        fig.show()
        return fig

    def __extract_urls(self, input_ids):
        df = self.__project_parser.to_dataframe()
        if not self.__project_parser.task_input_config["type"] in self.SUPPORTED_INPUT_TYPES:
            raise ValueError(f'The type {self.__project_parser.task_input_config["type"]} is not supported')

        task_input = f'{self.__project_parser.task_input_config["input"]}.{self.__project_parser.task_input_config["type"]}'
        image_urls = df[df[self.__project_parser.task_input_config['input_node_id']].isin(input_ids)][
            task_input].unique()
        return image_urls
