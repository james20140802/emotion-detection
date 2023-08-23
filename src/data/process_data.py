"""
    data 폴더 내의 존재하는 csv 파일들을 읽고 처리 과정을 거쳐 저장함.
"""

import os
import re
import importlib.util
from typing import Union

import pandas as pd


def get_load_files() -> list[str]:
    """
    src/data/load 내에 있는 python files들의 path를 반환함.

    Returns:
        list[str]: python files들의 path list.
    """
    current_path = os.path.dirname(os.path.abspath(__file__))
    load_py_path = os.path.join(current_path, "load")

    load_files = []
    for entry in os.scandir(load_py_path):
        if entry.name.endswith(".py") and entry.name.startswith("load"):
            load_files.append(entry.path)

    return load_files


def dynamic_load() -> Union[pd.DataFrame, int]:
    """
    data 폴더 내에 있는 csv files들에서 text data를 pd.Series로 반환함.

    Returns:
        Union[pd.DataFrame, int]

        pd.Series : 로드 결과물

        0 : 잘못된 format의 data가 발견

        -1 : 로드 과정 내 에러 발생
    """
    load_files = get_load_files()
    text_df_list = []

    for load_file in load_files:
        module_name = os.path.split(load_file)[-1].strip(".py")
        spec = importlib.util.spec_from_file_location(module_name, load_file)

        load_module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(load_module)

        try:
            text_df = load_module.load()
            assert isinstance(text_df, pd.Series), "invalid type"

            text_df_list.append(text_df)
        except AssertionError:
            return 0
        except AttributeError:
            return -1

    result = pd.concat(text_df_list, ignore_index=True)

    result.dropna(inplace=True)

    return result


def clean_text(text_series: pd.Series) -> pd.Series:
    """
    text data 속 url, hashtag 등 필요 없는 부분을 지움.

    Args:
        text_Series (pd.Series): input text data.

    Returns:
        pd.Series: cleaned text data.
    """
    text_series = text_series.apply(lambda x: x.lower())  # Lowercase

    text_series = text_series.apply(
        lambda x: re.sub(r"(?:\@|#|http?\://|https?\://|www)\S+", "", x)
    )  # URL, hashtag, mention 삭제

    text_series = text_series.apply(lambda x: re.sub(r"\W*\b\w{1}\b", "", x))  # 한 글자 단어 삭제

    text_series = text_series.apply(lambda x: re.sub("([.,!?()])", r" \1 ", x))
    text_series = text_series.apply(lambda x: re.sub(r"\s{2,}", " ", x))  # 구두점은 단어와 분리

    return text_series
