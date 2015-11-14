
import os

import pandas as pd

_BASE_PATH = os.path.dirpath(os.path.dirpath(__file__))
DATA_PATH = os.path.join(_BASE_PATH, 'data', 'DBscandataset.csv')


def load(dpath):

    return pd.read_csv(dpath)