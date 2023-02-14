import os
from datetime import datetime
import numpy as np
from scipy import stats
from typing import Any


DIR_NAME = 'data/'
SAMPLE_DIR = os.path.join(os.path.dirname(__file__), DIR_NAME)


def save_to_file(obj: Any, name: str):
    with open(SAMPLE_DIR + f'{name}_{datetime.now().date()}.txt', 'w') as outfile:
        outfile.write(obj)


def save_figure(obj: Any, ):
    with open(SAMPLE_DIR + f'fig_{datetime.now().date()}.png', 'w') as outfile:
        outfile.write(obj)


def return_base_statistics(data_: np.ndarray):
    mean = np.mean(data_)
    std = np.std(data_)
    sem = stats.sem(data_)
    min_ = min(data_)
    max_ = max(data_)
    return float(mean), float(sem), float(std), int(max_), int(min_)
