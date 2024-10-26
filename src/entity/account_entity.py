import pandas as pd

class Account:
    def __init__(self, name: str, fn: str, data: pd.DataFrame):
        self.acc_name = name
        self.filename = fn
        self.data = data
