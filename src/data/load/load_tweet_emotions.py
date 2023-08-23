"""
    data/raw 폴더 속 tweet_emotions.csv 의 text data를 로드함.
"""

import os

import pandas as pd


def load():
    """
    data/raw 폴더 속 tweet_emotions.csv 의 text data를 로드함.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "../../../data/raw/tweet_emotions.csv")

    dataframe = pd.read_csv(data_path)

    return dataframe.loc[:, "content"]
