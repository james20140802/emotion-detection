"""
    src/data/process_data.py 테스트    
"""

import os
import sys

import pandas as pd

application_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")
sys.path.append(application_path)


from src.data.process_data import clean_text


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
