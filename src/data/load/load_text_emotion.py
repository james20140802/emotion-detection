"""
    data/raw 폴더 속 Text_Emotion/train.csv 의 text data를 로드함.
"""

import os

import pandas as pd


def loada():
    """
    data/raw 폴더 속 Text_Emotion/train.csv 의 text data를 로드함.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "../../../data/raw/Text_Emotion/train.csv")

    dataframe = pd.read_csv(data_path)

    return dataframe.loc[:, "text"]
