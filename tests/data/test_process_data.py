"""
    src/data/process_data.py 테스트    
"""

import os
import sys

import pytest
import pandas as pd

application_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "../../"
)
sys.path.append(application_path)


from src.data.process_data import (
    get_load_files,
    dynamic_load,
    clean_text,
    save_processed_data,
)


def test_get_load_files():
    """
    test get_load_files function
    """

    load_files_path = get_load_files()

    is_path_exists = []
    for path in load_files_path:
        is_path_exists.append(os.path.exists(path))

    # check if return value is list and is valid
    assert isinstance(load_files_path, list) and all(is_path_exists)


@pytest.mark.filterwarnings("ignore::DeprecationWarning")
def test_dynamic_load():
    """
    test dynamic_load function
    """

    text_dataframe = dynamic_load()

    assert isinstance(text_dataframe, pd.Series)  # check if result if pd.Series


def test_clean_text():
    """
    test clean_text function
    """
    examples = pd.Series(
        [
            "@tif i know i was listenin to bad habit earlier and started freakin at his part =[",
            "worry,Hmmm. http://www.djhero.com/ is down",
            "Choked on her retainers",
        ]
    )
    answers = pd.Series(
        [
            " know was listenin to bad habit earlier and started freakin at his part =[",
            "worry , hmmm . is down",
            "choked on her retainers",
        ]
    )
    result = clean_text(examples)

    assert answers.equals(result)


def test_save_processed_data():
    """
    test save_processed_data function
    """
    save_processed_data()

    current_dir = os.path.dirname(os.path.abspath(__file__))
    processed_data_path = os.path.join(
        current_dir, "../../data/processed/processed_data.pkl"
    )

    if os.path.exists(processed_data_path):
        text_dataframe = pd.read_pickle(processed_data_path)

        assert isinstance(text_dataframe, pd.Series)
    else:
        assert False
