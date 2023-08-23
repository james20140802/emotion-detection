import os

import pandas as pd


def load():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "../../data/raw/tweet_emotions.csv")

    df = pd.read_csv(data_path)

    return df.loc[:, "content"]
