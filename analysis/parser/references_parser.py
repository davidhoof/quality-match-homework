import json
import os

import pandas as pd


class ReferenceParser:

    def __init__(self, file_path: str):
        """
        Project Parser parses a project references to different python formats
        :param file_path Path to the json file
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File path \"{file_path}\" could not be found")

        self.project_dict = {}
        with open(file_path, "r") as references_file:
            self.__references_dict = json.load(references_file)

        self.__references_dataframe = None

    def to_dataframe(self, cache=True) -> pd.DataFrame:
        """
        Parse references to pandas dataframe
        :return: pandas DataFrame
        """

        if self.__references_dataframe is None or cache is False:
            self.__references_dataframe = pd.DataFrame.from_records(
                self.__references_dict).transpose().reset_index().rename(
                columns={'index': 'img_name'})

        return self.__references_dataframe
