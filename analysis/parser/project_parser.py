import itertools
import json
import os

import pandas as pd

from analysis.utils.json_utils import get_by_path


class ProjectParser:
    """
    Project Parser parses a project to different python formats
    :param file_path Path to the json file
    :param tasks_path: json path configuration to access the tasks
    """

    def __init__(self, file_path: str, tasks_path=None, task_input_config=None):
        if tasks_path is not None and type(tasks_path) is not list:
            raise ValueError(f"tasks_path has to be None or list. Got {type(tasks_path)}")
        if tasks_path is None:
            tasks_path = ['results', 'root_node', 'results']

        if task_input_config is not None and type(task_input_config) is not dict:
            raise ValueError(f"tasks_path has to be None or list. Got {type(task_input_config)}")
        if task_input_config is None:
            self.task_input_config = {
                'input': 'task_input',
                'input_node_id': 'project_node_input_id',
                'type': 'image_url'
            }

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File path \"{file_path}\" could not be found")

        self.project_dict = {}
        with open(file_path, "r") as project_file:
            self.project_dict = get_by_path(json.load(project_file), tasks_path)

        self.__project_dataframe = None

    def to_dataframe(self, cache=True) -> pd.DataFrame:
        """
        Parse Project to pandas dataframe
        :param cache determines if the created dataframe is cached for faster usage
        :return: pandas DataFrame
        """

        if self.__project_dataframe is None or cache is False:
            self.__project_dataframe = pd.json_normalize(
                list(itertools.chain.from_iterable(
                    [self.project_dict[input_node_id]['results'] for input_node_id in self.project_dict.keys()]
                )))

        return self.__project_dataframe
