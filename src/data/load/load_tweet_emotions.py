"""
    data/raw 폴더 속 tweet_emotions.csv 의 text data를 로드함.
"""

import os

import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi


def load():
    """
    data/raw 폴더 속 tweet_emotions.csv 의 text data를 로드함.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(
        current_dir,
        "../../../data/raw/emotion-detection-from-text/tweet_emotions.csv",
    )

    # 만약 local에 데이터가 존재하지 않다면 kaggle에서 다운로드 받음.
    if not os.path.exists(data_path):
        api = KaggleApi()
        api.authenticate()

        download_dir = os.path.join(
            current_dir, "../../../data/raw/emotion-detection-from-text"
        )

        api.dataset_download_files(
            "pashupatigupta/emotion-detection-from-text",
            path=download_dir,
            unzip=True,
        )

    dataframe = pd.read_csv(data_path)

    return dataframe.loc[:, "content"]
