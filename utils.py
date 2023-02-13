import os
from datetime import datetime
from typing import Any


DIR_NAME = 'data/'
SAMPLE_DIR = os.path.join(os.path.dirname(__file__), DIR_NAME)


def save_to_file(obj: Any, name: str):
    with open(SAMPLE_DIR + f'{name}_{datetime.now().date()}.txt', 'w') as outfile:
        outfile.write(obj)


def save_figure(obj: Any, ):
    with open(SAMPLE_DIR + f'fig_{datetime.now().date()}.png', 'w') as outfile:
        outfile.write(obj)
