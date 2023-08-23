import os
import importlib.util
from typing import Union

import pandas as pd


def get_load_files() -> list[str]:
    current_path = os.path.dirname(os.path.abspath(__file__))
    load_py_path = os.path.join(current_path, "load")

    load_files = []
    for entry in os.scandir(load_py_path):
        if entry.name.endswith(".py") and entry.name.startswith("load"):
            load_files.append(entry.path)

    return load_files


def dynamic_load() -> Union[pd.DataFrame, int]:
    load_files = get_load_files()
    text_df_list = []

    for load_file in load_files:
        module_name = os.path.split(load_file)[-1].strip(".py")
        spec = importlib.util.spec_from_file_location(module_name, load_file)

        load_module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(load_module)

        try:
            text_df = load_module.load()
            assert type(text_df) == pd.Series, "invalid type"

            text_df_list.append(text_df)
        except AssertionError:
            return 0
        except:
            return -1

    result = pd.concat(text_df_list, ignore_index=True)

    result.dropna(inplace=True)

    return result
