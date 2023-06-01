"""Airbus SPOT image meta data"""
import os
import pandas as pd

import logging
import logging.config
logging.config.fileConfig('logging.ini')

class airbus_meta:
    """Pre-process meta data"""

    def __init__(self)-> None:
        pass

    def read_annotations(self):
        """Read the annotations csv"""
        self.annots_csv = os.path.join(
            os.environ.get('AIRBUS_SPOT'),
            'annotations.csv')
        self.df = pd.read_csv(self.annots_csv, header = 0)
        print(self.df.head())
        return self.df